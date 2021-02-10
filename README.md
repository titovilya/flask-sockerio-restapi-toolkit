Developers documentation v 1.0

1. GIT
    1. git checkout <namebranch>
    2. git pull origin master
    3. git commit -m '<urname>/<info>'
    4. git push

    To add sm-th new: create a new branch.
    1.1 git branch -m '<urname>/<info>'

    MERGE SOLVING!
    git stash save
    git pull origin/master
    git stash pop

2. Flask+docker commands

    1. To enter in container:
    docker exec -it <container_name> bash

3. How to close connection between docker and www:
    https://docs.docker.com/network/iptables/
    https://qastack.ru/server/704643/steps-for-limiting-outside-connections-to-docker-container-with-iptables
    Another way: JWT TOKEN.

4. Vesta data:
    login: root
    password: test007

CHANGE SERVERNAME nginx/nginx_dev.conf and nginx/nginx_prod.conf
CHANGE SSL Sertificates nginx/dev_crts and nginx/prod_crts
CHANGE mainpage/app/init servername