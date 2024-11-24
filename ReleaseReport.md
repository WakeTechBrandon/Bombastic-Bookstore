CSC289 Programming Capstone Project

Project Name: {Bombastic Bookstore}
Team Number: {#2}
Team Project Manager: {Brandon Biggs}
Team Members: {***Julia McDonald, Jaylan Chavis, James Dove, Joshua Macy, Ryan Burres***}

 
Release Report

 [Bombastic Bookstore] - Version [v1.0.0]


Overview

This release report provides an overview of the development, testing, and deployment process for Version 1.0.0 of our new software project, Bombastic Bookstore. The release marks the successful completion of the initial phase of development and the launch of the application to production. Bombastic Bookstore aims to be an inventory management software for a bookstore owner. 

Development Highlights

Project Kickoff: The project officially started on August 30, 2024, with the formation of the development team and the kickoff meeting to discuss project goals, scope, and timeline. 

Requirements Gathering: The team conducted thorough requirements gathering sessions to define the features and functionalities of the software application. Technologies and team knowledge gaps were assessed. Appropriate learning resources were distributed to team members, such as links to Django tutorials.

Design and Architecture: The software architecture and design were finalized, including database schema and system components. The team decided to use the Django web framework to create the inventory application.  Sqlite was chosen as the database system along with the Django built-in user access control functions to manage login. The team decided the application should be minimalist, with ease-of-access, and have full CRUD (create, read, update, delete) abilities based on user responsibilities.


Development 

Sprint: Development proceeded in multiple sprints, each lasting two weeks, with a focus on implementing specific features and user stories. The sprints were organized as follows:
    - Sprint 1: Setting up the models and related back-end functions
    - Sprint 2: Core front-end functions and templates
    - Sprint 3: Completing back-end development
    - Sprint 4: Completing front-end development
    - Sprint 5: Refinement and styling

Some milestones achieved:
    - Setting up Django environment
    - SQL database setup
    - Creating and displaying first webpages
    - Creating login system
    - Making webpages interactive and dynamic
    - finalized features (searching, filtering, removing etc)
    - Creating theme customization

Challenges faced:
    - Knowledge gaps
    - Scheduling conflicts

Code Reviews and Testing: Regular code reviews were conducted to ensure code quality and adherence to coding standards. Manual/integration testing was used to validate functionality. Github's pull-request review feature was used to allow multiple team members to review all code changes.


Deployment

Staging Environment: The application was deployed independently by each team member throughout development using Django's built-in server functionality.

Production Deployment: After successful testing in the staging environment, the application was packaged into a batch installation file ready to be distributed to users for use.
 

Release Notes

New Features:

This the first release. All features are new, including the abilites to create/delete new stock items and manage quantities of existing stock items.

Bug Fixes:

Several error catching methods were implemented to avoid http status code 404 errors.  Scalable UI components were added to allow adaptable screen types.

Known Issues:

Filtering options are currently limited to author and category.  Search option isn't advanced enough to allow narrowing down results to find the most relevant results.


Conclusion

The release of Version 1.0.0 of Bombastic Bookstore represents a significant milestone in the project's development journey. The project team has worked diligently to deliver a high-quality software application that meets the needs and expectations of our users. We look forward to continued feedback and collaboration as we work towards future releases and enhancements.

This release report provides stakeholders with an overview of the development process, testing efforts, deployment activities, and key highlights for Version 1.0.0 of Bombastic Bookstore. It serves as a record of the project's progress and achievements, highlighting the successful completion of the initial phase of development and the launch of the application to production.