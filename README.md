# 🚀 Automatisation d'une instance EC2 via une interface Web

Ce projet permet de lancer automatiquement une instance EC2 sur AWS via une **interface web simple** construite avec **Flask**.  
L'infrastructure réseau (VPC, subnet, sécurité...) est automatiquement créée grâce à **Terraform**.

---

## 🛠️ Technologies utilisées

- Python 3 / Flask
- Jinja2 (pour les templates Terraform)
- Terraform
- AWS (EC2, VPC, etc.)

---

## 🖥️ Fonctionnalités

- Formulaire HTML (nom, AMI, type d’instance)
- Génération dynamique du fichier Terraform (`main.tf`)
- Création automatique d’une infrastructure complète :
  - VPC
  - Subnet public
  - Internet Gateway
  - Groupe de sécurité
  - Instance EC2

---

## 📦 Installation et utilisation

### 1. Cloner le projet

```bash
git clone https://github.com/Creepy4Bbby/Automatisation-d-une-EC2-depuis-une-interface-Web.git
cd Automatisation-d-une-EC2-depuis-une-interface-Web

python3 -m venv venv
source venv/bin/activate

pip install flask jinja2

Ensuite, ouvre ton navigateur sur :
👉 http://localhost:5000

⚙️ Prérequis

    ✅ Compte AWS avec clés configurées (aws configure)

    ✅ Terraform installé : https://developer.hashicorp.com/terraform/downloads

    ✅ Python 3


    📁 Structure du projet

aws_project/
├── app.py
├── templates/
│   └── form.html
├── terraform/
│   ├── main.tf.j2
│   └── variables.tf
├── venv/ (non versionné)
└── .gitignore



🧾 Exemple d’utilisation

    Lancer le serveur Flask

    Remplir le formulaire web :

        Nom d’instance

        AMI (ex. Debian 12)

        Type d’instance (ex. t2.micro)

    L’application crée :

        Le réseau (VPC, subnet, etc.)

        L’instance EC2 automatiquement via Terraform

👤 Auteur

Creepy4Bbby
Automatisation de l’infrastructure cloud avec une interface intuitive 🧠💻
