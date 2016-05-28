# qna-iitk
An intranet General-purpose Question and Answer website
##              ONLY FOR IITK STUDENTS
##Structure
    The site runs on a python backend with Django framework. The project is divided into 2 apps:
    1. accounts - Contains User profile and Custom User models, views, urls, forms and templates.
    2. qna - The app responsible for the question-answer functonality. This has the following models:
        1. Question
        2. Answer
        3. Comment
        4. Upvote
##Progress
    I had some difficulty setting up a custom backend for authenticating and creating user entries from the IITK database, which consisted of authenticating IITK username and password against the intranet FTP server, and scrapinf resulting user data from the Office Automation Portal to autocomplete key user entries. Hopefully the base will be ready in a few days.
    The frontend design is being discussed and will most probably use [MaterializeCSS] framework(materializecss.com).

