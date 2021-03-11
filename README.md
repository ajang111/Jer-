# Student Network - Reconnect

A student network which promotes interaction within the University of Exeter's
student community. This aims to provide social opportunities by encouraging
students to engage with each other in a fun and friendly online environment.

## Group N - Contributors

Group members (contributors) include:

- Isaac Cheng
- Ryan Storey
- Sofia Reid
- Barnie Gill
- Oskar Oramus
- Sam Shailer

## Live Deployed Version

This application has been deployed on Amazon Web Services (AWS). You can access
it with the following link:

[http://reconnect-env.eba-6cuvfzp3.eu-west-2.elasticbeanstalk.com](http://reconnect-env.eba-6cuvfzp3.eu-west-2.elasticbeanstalk.com)

## User Guide

Upon opening the application, you will be greeted with a home page. From here,
you can log into your existing account, or you can register a new account. It
should be noted that registration will only work with University of Exeter
email addresses, and academics will be sent for manual verification after
signing up.

When you log in, you will be redirected to your profile page. This displays
information about you, such as your hobbies, interests, your rarest
achievements unlocked, and links to your social media profiles. Posts made by
you are also displayed on this page.

By default, some details will be filled in for you, such as your profile
picture, bio, date of birth, and gender. You can edit all these details by
pressing the 'Edit Profile' button.

To search for other members on the Reconnect network, you can navigate to the
'Members' page using the navigation bar on the top. From here, you can search
by the username, with the option of searching by a common hobby and/or interest
too. Search results will be displayed live with their username and their
degree, enabling you to visit the profiles of people and make connections.

Connections may be formed with people, with the option of marking connections
as close friends. Whereas connections must be accepted by people, you are able
to mark people as close friends without making a request. This also means that
a user may be your close friend, but you may not be their close friend; the
close friend system is one-way. If you wish to limit interaction with another
user, then you can block them. All these options may be accessed by navigating
to a user's profile.

You can view a list of your connections and pending connection requests on the
Connections page. Users who you have marked as a close friend have an icon of a
handshake next to them.

On your feed, you can view all the posts of people who you have connected with.
This is sorted in chronological order, with the newest posts appearing at the
top. You can also make new posts from this page; these are categorised as a
text post, an image post, or a link post.

Achievements may be unlocked by performing tasks on the Reconnect network. You
can view these on the Achievements page, which displays your progress with
achievements as a percentage, and the achievements you have completed, starting
from the most recent. This page also shows you which achievements you are yet
to unlock. Hovering over each achievement shows the title of the achievement,
description, and number of XP gained by unlocking it. Each of these
achievements has its own unique icon. Watch out for hidden achievements which
are not displayed until you unlock them; these will reward you with extra XP!

You will level up your profile based on how much XP you have gained. This
encourages some healthy competition in the Reconnect network. By interacting
more in various parts of the application, you will quickly be able to climb up
the leaderboard!

We have also provided you with an easy way to test and share your knowledge on
the Quizzes page. From here, you can create a quiz consisting of five
multiple-choice questions for others to complete. You can also view and take
part in quizzes made from other people.

## Test Instructions

For testing purposes, we have created a lot of accounts and sample data to make
it easier to demo the product. This includes the users `barn354` and `ic324`,
both with password `Password01`, have been set up with a full student profile
and multiple posts.

## GitHub Repository

The documentation and source files for our project can be found in our GitHub
repository as follows:

[https://github.com/IsaacCheng9/student-network](https://github.com/IsaacCheng9/student-network)

### Process Documents

Project management is handled using the Kanban methodology through a Trello
board, which can be found below:

[https://trello.com/b/xnKnkaxg/gsep-group-n](https://trello.com/b/xnKnkaxg/gsep-group-n)

We have taken regular snapshots of the Kanban board in Trello to archive our
progress. These can be found in the following path of the repository:

[./process-documents/kanban-snapshots](./process-documents/kanban-snapshots)

In addition, minutes have been recorded for every group meeting. They can be
found in the following path:

[./process-documents/meeting-notes](./process-documents/meeting-notes)

### Product Documents

These documents involve requirements analysis, which has been encapsulated
through our research documents on potential solutions, design thinking plan,
and MoSCoW matrix.

They can be found in the following path:

[./product-documents](./product-documents)

### Technical Documents

Technical documents consist of source code, broken down into the front-end and
back-end files.

They can be found in the following path:

[./technical-documents](./technical-documents)

## Prerequisites

### Python Version

The application has been developed and tested to work on Python 3.8 and
onwards.

### Python Libraries

This project uses several Python libraries. To run the application locally, you
should `pip install` the following:

- click
- email-validator
- Flask
- itsdangerous
- Jinja2
- MarkupSafe
- passlib
- Werkzeug
- Pillow

For example, you should `pip install passlib`.

### Virtual Environment

Alternatively, a virtual environment has been included in the GitHub
repository. This includes all the Python libraries required to run the
application locally.
