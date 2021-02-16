# adiciona repo e da push
heroku git:remote -a testcelero
git push heroku master

# env var
heroku config # obten as variaveis de ambiente

# setando vars
heroku config:set SECRET_KEY="abc" DJANGO_SETTINGS_MODULE="config.settings.prod"

# executando comandos
heroku run <command>
