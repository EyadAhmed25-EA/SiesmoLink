SeismoLink — Solar Powered Earthquake Alert System

SeismoLink is a solar-powered, internet-independent earthquake detection and alert system designed to serve vulnerable and remote communities with limited infrastructure. The project was developed in March 2025 by a four-member team at Hack Without Borders, with a focus on accessibility, reliability, and real-world deployment feasibility.

The system combines satellite image analysis, edge computing, and off-grid hardware to provide rapid, accessible earthquake alerts without relying on traditional internet connectivity.

Project Motivation

In regions such as Haiti, earthquake detection and alert systems are often inaccessible due to unreliable power and internet infrastructure. SeismoLink was designed to:
	•	Operate fully off-grid
	•	Detect seismic displacement using satellite imagery
	•	Provide accessible alerts for all users
	•	Support scalable real-world deployment

System Overview

SeismoLink analyzes ground displacement using satellite GeoTIFF images captured before and after seismic activity.

Detection Algorithm

	•	Developed in Python using the Thonny IDE
	•	Performs pixel-wise subtraction between two GeoTIFF images
	•	Applies a 1 cm displacement threshold
	•	If 50+ pixels exceed the threshold, the system triggers an earthquake alert

This method allows the system to identify significant land movement while filtering out minor noise and inconsistencies.

Hardware Architecture

	•	Raspberry Pi as the main processing unit
	•	Solar panel power system with battery backup
	•	Fully functional without internet connectivity
	•	Designed for continuous off-grid operation

Alert System

To ensure accessibility:
	•	Audio alerts for immediate notification
	•	Visual alerts for users with hearing impairments

This dual-alert approach ensures the system can be used safely by individuals with different accessibility needs.

Design & Prototyping

The team designed a 3D CAD enclosure model for:
	•	Device layout planning
	•	Component organization
	•	Scalable prototyping
	•	Real-world deployment preparation

This allowed the system to be visualized as a deployable physical product rather than only a software prototype.

Technology Stack

	•	Python (Image analysis and detection algorithm)
	•	Thonny IDE
	•	Solar panel + battery system
	•	Satellite GeoTIFF imagery
	•	3D CAD modeling software

Key Features

	•	Internet-independent operation
	•	Solar powered with battery backup
	•	Satellite image-based displacement detection
	•	Threshold-based alert triggering
	•	Accessible audio and visual alerts
	•	Portable and scalable hardware design



🔒 Repository Note

This repository documents the system design, detection logic, and hardware integration for academic and research demonstration purposes.



If you’d like, I can also generate:
	•	A system architecture diagram description section
	•	A setup / installation guide
	•	A resume-optimized project summary
	•	Or a technical algorithm breakdown section
