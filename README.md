# 🛡️ Digital Footprint Visualizer

### App-Specific Permissions + Weighted Risk Analysis

**Digital Footprint Visualizer** is an educational cybersecurity and privacy-awareness application designed to help users understand their potential digital exposure through the apps they use, permissions they grant, and their everyday digital habits.

The application transforms user-provided information into an interactive exposure profile using **weighted risk analysis, visual dashboards, network visualization, and personalized recommendations.**

---

## 🎯 Problem Statement

Modern users interact with numerous applications that may request access to sensitive resources such as:

*  Camera
*  Microphone
*  Location
*  Contacts
* Storage & Photos
*  SMS
*  Calendar
*  Files
*  Advertising / Tracking IDs

Individually, these permissions may seem harmless. However, the combination of multiple applications, permissions, and digital habits can create a broader digital exposure profile.

**Digital Footprint Visualizer** provides an educational way to visualize these relationships and identify areas that may deserve greater privacy and security attention.

---

## 💡 Project Objective

The primary objective of this project is to provide an easy-to-understand visualization of a user's digital footprint rather than presenting privacy and cybersecurity risks as isolated technical concepts.

The application aims to:

* Identify applications used by the user
* Map applications to sensitive permissions
* Calculate an educational exposure score
* Highlight major exposure contributors
* Visualize relationships between apps and permissions
* Provide personalized privacy and security recommendations
* Encourage better digital security habits

---

##  Key Features

###  App-Level Digital Footprint Analysis

Users can select the applications and platforms they actively use across categories such as:

* Social & Media
* Messaging & Calls
* AI Assistants
* Shopping & Finance
* Entertainment
* Productivity & Cloud

---

###  Permission Mapping

The application allows users to specify which applications have access to sensitive permissions including:

* Camera
* Microphone
* Location
* Contacts
* Storage / Photos
* SMS
* Calendar
* File Access
* Advertising / Tracking ID

This creates an **app-permission relationship map** for the user's digital footprint.

---

###  Weighted Exposure Analysis

Instead of treating every permission equally, the application uses:

**Permission Base Points × App Risk Weight**

to calculate an educational risk contribution for each app-permission combination.

This allows the model to distinguish between different combinations rather than simply counting the number of permissions.

---

### 📊 Interactive Exposure Dashboard

The application generates an overall **Exposure Surface Score** and classifies the resulting profile into:

* 🟢 Low Data Exposure
* 🟡 Moderate Data Exposure
* 🔴 High Data Exposure

The dashboard also displays the number of app-permission relationships contributing to the user's profile.

---

###  Interactive Visualizations

The project provides multiple visual representations of the assessment:

* Top risk contributors
* Exposure by permission type
* Exposure by application category
* App-wise risk contribution
* General digital activity

These visualizations make the assessment easier to interpret than a numerical score alone.

---

###  Digital Footprint Network

The application creates an interactive network representation showing relationships between:

**User → Applications → Permissions**

This visualization helps demonstrate how multiple applications can connect to different categories of sensitive access.

---

### Personalized Recommendations

Based on the user's responses, the application generates recommendations related to:

* Application permissions
* Two-Factor Authentication
* Password reuse
* Public Wi-Fi
* Unknown-source applications
* Screen time
* Installed applications
* Notifications
* Cloud storage
* Bluetooth usage

---

###  Digital Security Habits

The application also identifies positive security practices such as:

* Two-Factor Authentication
* Avoiding password reuse
* Using a VPN
* Avoiding unknown application sources
* Limiting unnecessary permissions

---

###  CSV Export

Users can download their entered assessment information and permission matrix as a CSV file for further analysis or record keeping.

---

#  How the Application Works

```text
                 USER INPUT
                     │
                     ▼
          ┌─────────────────────┐
          │ Apps & Platforms    │
          │ Digital Habits      │
          │ Security Practices  │
          └──────────┬──────────┘
                     │
                     ▼
          ┌─────────────────────┐
          │ Permission Mapping  │
          │ Camera              │
          │ Location            │
          │ Microphone          │
          │ Contacts etc.       │
          └──────────┬──────────┘
                     │
                     ▼
          ┌─────────────────────┐
          │ Weighted Exposure   │
          │ Analysis Engine     │
          └──────────┬──────────┘
                     │
          ┌──────────┼──────────┐
          ▼          ▼          ▼
       Score      Charts     Network
          │          │          │
          └──────────┼──────────┘
                     ▼
          Personalized Advice
```

---

#  Risk Analysis Model

The project uses an educational weighted scoring approach.

For an app-permission combination:

```text
Risk Contribution
        =
Permission Base Points × App Risk Weight
```

Additional points may be contributed by selected digital habits and security conditions.

The final exposure score is then used to categorize the user's profile into different exposure levels.

> **Important:** The weights and thresholds are model parameters created for this educational project. They should not be interpreted as an official cybersecurity risk standard.

---

#  Technology Stack

| Technology    | Purpose                                |
| ------------- | -------------------------------------- |
| **Python**    | Core application logic                 |
| **Streamlit** | Interactive web application            |
| **Pandas**    | Data processing and tabular analysis   |
| **Plotly**    | Interactive charts and visualizations  |
| **NetworkX**  | Digital footprint network construction |

---

#  Application Structure

The application is organized into five major sections:

###  Overview

Provides the overall exposure score, exposure classification, applications used, and digital profile.

###  Charts

Displays the major contributors and different views of exposure across permissions, applications, and activity.

###  Network

Visualizes the relationship between the user, applications, and sensitive permissions.

###  Advice & Habits

Displays major exposure contributors, personalized recommendations, and positive security practices.

###  Raw Data

Displays the entered assessment information and the app-permission matrix, with an option to export the data as CSV.


# 🛡️ Digital Footprint Visualizer

### App-Specific Permissions + Weighted Risk Analysis

**Digital Footprint Visualizer** is an educational cybersecurity and privacy-awareness application designed to help users understand their potential digital exposure through the apps they use, permissions they grant, and their everyday digital habits.

The application transforms user-provided information into an interactive exposure profile using **weighted risk analysis, visual dashboards, network visualization, and personalized recommendations.**

---

## 🎯 Problem Statement

Modern users interact with numerous applications that may request access to sensitive resources such as:

* 📷 Camera
* 🎤 Microphone
* 📍 Location
* 👥 Contacts
* 🗂️ Storage & Photos
* ✉️ SMS
* 📅 Calendar
* 📁 Files
* 🎯 Advertising / Tracking IDs

Individually, these permissions may seem harmless. However, the combination of multiple applications, permissions, and digital habits can create a broader digital exposure profile.

**Digital Footprint Visualizer** provides an educational way to visualize these relationships and identify areas that may deserve greater privacy and security attention.

---

## 💡 Project Objective

The primary objective of this project is to provide an easy-to-understand visualization of a user's digital footprint rather than presenting privacy and cybersecurity risks as isolated technical concepts.

The application aims to:

* Identify applications used by the user
* Map applications to sensitive permissions
* Calculate an educational exposure score
* Highlight major exposure contributors
* Visualize relationships between apps and permissions
* Provide personalized privacy and security recommendations
* Encourage better digital security habits

---

## ✨ Key Features

### 📱 App-Level Digital Footprint Analysis

Users can select the applications and platforms they actively use across categories such as:

* Social & Media
* Messaging & Calls
* AI Assistants
* Shopping & Finance
* Entertainment
* Productivity & Cloud

---

### 🔐 Permission Mapping

The application allows users to specify which applications have access to sensitive permissions including:

* Camera
* Microphone
* Location
* Contacts
* Storage / Photos
* SMS
* Calendar
* File Access
* Advertising / Tracking ID

This creates an **app-permission relationship map** for the user's digital footprint.

---

### ⚖️ Weighted Exposure Analysis

Instead of treating every permission equally, the application uses:

**Permission Base Points × App Risk Weight**

to calculate an educational risk contribution for each app-permission combination.

This allows the model to distinguish between different combinations rather than simply counting the number of permissions.

---

### 📊 Interactive Exposure Dashboard

The application generates an overall **Exposure Surface Score** and classifies the resulting profile into:

* 🟢 Low Data Exposure
* 🟡 Moderate Data Exposure
* 🔴 High Data Exposure

The dashboard also displays the number of app-permission relationships contributing to the user's profile.

---

### 📈 Interactive Visualizations

The project provides multiple visual representations of the assessment:

* Top risk contributors
* Exposure by permission type
* Exposure by application category
* App-wise risk contribution
* General digital activity

These visualizations make the assessment easier to interpret than a numerical score alone.

---

### 🕸️ Digital Footprint Network

The application creates an interactive network representation showing relationships between:

**User → Applications → Permissions**

This visualization helps demonstrate how multiple applications can connect to different categories of sensitive access.

---

### 💡 Personalized Recommendations

Based on the user's responses, the application generates recommendations related to:

* Application permissions
* Two-Factor Authentication
* Password reuse
* Public Wi-Fi
* Unknown-source applications
* Screen time
* Installed applications
* Notifications
* Cloud storage
* Bluetooth usage

---

### 🏆 Digital Security Habits

The application also identifies positive security practices such as:

* Two-Factor Authentication
* Avoiding password reuse
* Using a VPN
* Avoiding unknown application sources
* Limiting unnecessary permissions

---

### 📥 CSV Export

Users can download their entered assessment information and permission matrix as a CSV file for further analysis or record keeping.

---

# 🔄 How the Application Works

```text
                 USER INPUT
                     │
                     ▼
          ┌─────────────────────┐
          │ Apps & Platforms    │
          │ Digital Habits      │
          │ Security Practices  │
          └──────────┬──────────┘
                     │
                     ▼
          ┌─────────────────────┐
          │ Permission Mapping  │
          │ Camera              │
          │ Location            │
          │ Microphone          │
          │ Contacts etc.       │
          └──────────┬──────────┘
                     │
                     ▼
          ┌─────────────────────┐
          │ Weighted Exposure   │
          │ Analysis Engine     │
          └──────────┬──────────┘
                     │
          ┌──────────┼──────────┐
          ▼          ▼          ▼
       Score      Charts     Network
          │          │          │
          └──────────┼──────────┘
                     ▼
          Personalized Advice
```

---

# 🧮 Risk Analysis Model

The project uses an educational weighted scoring approach.

For an app-permission combination:

```text
Risk Contribution
        =
Permission Base Points × App Risk Weight
```

Additional points may be contributed by selected digital habits and security conditions.

The final exposure score is then used to categorize the user's profile into different exposure levels.

> **Important:** The weights and thresholds are model parameters created for this educational project. They should not be interpreted as an official cybersecurity risk standard.

---

# 🛠️ Technology Stack

| Technology    | Purpose                                |
| ------------- | -------------------------------------- |
| **Python**    | Core application logic                 |
| **Streamlit** | Interactive web application            |
| **Pandas**    | Data processing and tabular analysis   |
| **Plotly**    | Interactive charts and visualizations  |
| **NetworkX**  | Digital footprint network construction |

---

# 🖥️ Application Structure

The application is organized into five major sections:

### 🏠 Overview

Provides the overall exposure score, exposure classification, applications used, and digital profile.

### 📊 Charts

Displays the major contributors and different views of exposure across permissions, applications, and activity.

### 🕸️ Network

Visualizes the relationship between the user, applications, and sensitive permissions.

### 💡 Advice & Habits

Displays major exposure contributors, personalized recommendations, and positive security practices.

### 📋 Raw Data

Displays the entered assessment information and the app-permission matrix, with an option to export the data as CSV.

---

# 📸 Project Preview

## Landing Page

![Landing Page](screenshots/landing-page.png)

## Exposure Overview

![Overview](screenshots/overview.png)

## Risk Analysis

![Charts](screenshots/charts.png)

## Digital Footprint Network

![Network](screenshots/network.png)

## Recommendations

![Recommendations](screenshots/recommendations.png)

---

# 🚀 Running the Project

### 1. Clone the repository

```bash
git clone <repository-url>
cd digital-footprint-visualizer
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit application

```bash
streamlit run final_app1.py
```

> **Note:** The complete source implementation is not publicly distributed in this portfolio repository. The commands above describe the intended local execution structure if the source is provided separately.

---

# 👩‍💻 Project Contribution

This project involved the development and integration of:

* Streamlit application interface
* App and permission input system
* Weighted exposure analysis
* Interactive visualizations
* Network representation
* Personalized recommendations
* Digital security habit analysis
* CSV data export
* Presentation-oriented dashboard design

---

# 🎓 Project Context

**Type:** Academic / Educational Project
**Domain:** Cybersecurity & Privacy Awareness
**Platform:** Web-based Streamlit Application
**Primary Language:** Python

---

# ⚠️ Disclaimer

This project is an **educational risk-awareness model created for academic purposes**.

The exposure score and application risk weights are approximations based on general, publicly known data practices. They are **not an audit of any specific application's actual behavior** and do not represent the real-time permissions granted on a user's device.

The application should therefore be used for **educational awareness and exploration**, rather than as a professional cybersecurity assessment or privacy audit.

---

# 🔐 Source Code & Usage

The complete source implementation is **not publicly distributed** through this repository.

This repository is intended to document and demonstrate the project for **academic, portfolio, and educational purposes**.

The project materials and implementation remain the intellectual property of the author unless otherwise stated.

---

# 📌 Project Status

**Completed — Academic / Educational Project**

---

### 🛡️ Digital Footprint Visualizer

**Visualize your digital exposure. Understand your permissions. Build better security habits.**


# 👩‍💻 Project Contribution

This project involved the development and integration of:

* Streamlit application interface
* App and permission input system
* Weighted exposure analysis
* Interactive visualizations
* Network representation
* Personalized recommendations
* Digital security habit analysis
* CSV data export
* Presentation-oriented dashboard design

---

# 🎓 Project Context

**Type:** Academic / Educational Project
**Domain:** Cybersecurity & Privacy Awareness
**Platform:** Web-based Streamlit Application
**Primary Language:** Python

---

# ⚠️ Disclaimer

This project is an **educational risk-awareness model created for academic purposes**.

The exposure score and application risk weights are approximations based on general, publicly known data practices. They are **not an audit of any specific application's actual behavior** and do not represent the real-time permissions granted on a user's device.

The application should therefore be used for **educational awareness and exploration**, rather than as a professional cybersecurity assessment or privacy audit.

---

# 🔐 Source Code & Usage

The complete source implementation is **not publicly distributed** through this repository.

This repository is intended to document and demonstrate the project for **academic, portfolio, and educational purposes**.

The project materials and implementation remain the intellectual property of the author unless otherwise stated.

---

# 📌 Project Status

**Completed — Academic / Educational Project**

---

### 🛡️ Digital Footprint Visualizer

**Visualize your digital exposure. Understand your permissions. Build better security habits.**
