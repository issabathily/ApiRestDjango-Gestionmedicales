# 🏥 Système de Gestion Médicale

Un système de gestion médicale complet développé avec **Django** et **Django REST Framework** pour gérer les patients, les rendez-vous et les dossiers médicaux de manière sécurisée et efficace.

---

## 🚀 Fonctionnalités

- 🔐 Authentification sécurisée via token
- 👥 Gestion des utilisateurs avec rôles :
  - Administrateur
  - Médecin
  - Infirmier
  - Patient
- 🗂 Gestion des dossiers médicaux
- 🩺 Gestion des patients
- 📆 Prise de rendez-vous
- ⚙️ Interface d'administration via Django Admin

---

## ⚙️ Installation

1. **Créer un environnement virtuel** :

   ```bash
   python -m venv venv
   source venv/bin/activate  # macOS / Linux
   venv\Scripts\activate     # Windows
   ```

2. **Installer les dépendances** :

   ```bash
   pip install -r requirements.txt
   ```

3. **Configurer la base de données** :

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Créer un superutilisateur** :

   ```bash
   python manage.py createsuperuser
   ```

5. **Lancer le serveur** :

   ```bash
   python manage.py runserver
   ```

---

## 🧱 Structure du Projet

```
gestionmedical/
├── gestionmedical/         # Configuration principale du projet
├── medical/                # Application principale
│   ├── admin.py            # Configuration de l'interface d'admin
│   ├── models.py           # Définition des modèles
│   ├── permissions.py      # Permissions personnalisées
│   ├── serializers.py      # Sérialiseurs pour l'API
│   ├── urls.py             # Définition des routes API
│   └── views.py            # Vues pour les endpoints REST
└── requirements.txt        # Fichier des dépendances
```

---

## 🔗 Endpoints API

### 1. Authentification

**POST** `/api/api-token-auth/`

- **Body** :
  ```json
  {
      "username": "votre_username",
      "password": "votre_mot_de_passe"
  }
  ```

- **Réponse** :
  ```json
  {
      "token": "votre_token",
      "user_id": 1,
      "email": "votre_email"
  }
  ```

---

### 2. Profils Utilisateurs

#### GET `/api/profiles/`

- **Headers** : `Authorization: Token VOTRE_TOKEN`
- **Réponse** :
  ```json
  [
      {
          "id": 1,
          "role": "doctor",
          "phone": "1234567890"
      }
  ]
  ```

#### POST `/api/profiles/`

- **Headers** : `Authorization: Token VOTRE_TOKEN`
- **Body** :
  ```json
  {
      "role": "doctor",
      "phone": "1234567890"
  }
  ```

---

### 3. Patients

#### GET `/api/patients/`

- **Headers** : `Authorization: Token VOTRE_TOKEN`
- **Réponse** :
  ```json
  [
      {
          "id": 1,
          "date_of_birth": "1990-01-01",
          "blood_type": "O+",
          "allergies": "Pollen"
      }
  ]
  ```

#### POST `/api/patients/`

- **Headers** : `Authorization: Token VOTRE_TOKEN`
- **Body** :
  ```json
  {
      "date_of_birth": "1990-01-01",
      "blood_type": "O+",
      "allergies": "Pollen"
  }
  ```

---

### 4. Dossiers Médicaux

#### GET `/api/medical-records/`

- **Headers** : `Authorization: Token VOTRE_TOKEN`
- **Réponse** :
  ```json
  [
      {
          "id": 1,
          "patient": 1,
          "doctor": 2,
          "diagnosis": "Diabète",
          "treatment": "Insuline"
      }
  ]
  ```

#### POST `/api/medical-records/`

- **Headers** : `Authorization: Token VOTRE_TOKEN`
- **Body** :
  ```json
  {
      "patient": 1,
      "doctor": 2,
      "diagnosis": "Diabète",
      "treatment": "Insuline"
  }
  ```

---

### 5. Rendez-vous

#### GET `/api/appointments/`

- **Headers** : `Authorization: Token VOTRE_TOKEN`
- **Réponse** :
  ```json
  [
      {
          "id": 1,
          "patient": 1,
          "doctor": 2,
          "date": "2025-05-22T14:30:00Z",
          "status": "scheduled",
          "notes": "Première consultation"
      }
  ]
  ```

#### POST `/api/appointments/`

- **Headers** : `Authorization: Token VOTRE_TOKEN`
- **Body** :
  ```json
  {
      "patient": 1,
      "doctor": 2,
      "date": "2025-05-22T14:30:00Z",
      "notes": "Première consultation"
  }
  ```

---

## 🔐 Permissions

| Rôle         | Accès Patient | Accès Dossier Médical | Accès Rendez-vous |
|--------------|----------------|------------------------|--------------------|
| Admin        | ✅ Tous        | ❌                    | ✅ Tous           |
| Médecin      | ✅ Ses patients| ✅ Modifier           | ✅ Ses patients    |
| Infirmier    | ✅             | ✅ Lecture seule       | ✅                |
| Patient      | ✅ Lui-même     | ❌                    | ✅ Ses rendez-vous|

---

## 🧪 Tests avec Postman

1. **Authentification** :
   ```json
   {
       "username": "votre_username",
       "password": "votre_mot_de_passe"
   }
   ```

2. **Headers pour toutes les requêtes protégées** :
   ```
   Authorization: Token VOTRE_TOKEN
   ```

---

## 🛠️ Technologies Utilisées

- Django 5.x
- Django REST Framework
- SQLite / PostgreSQL
- Python 3.8+

---
