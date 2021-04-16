Bitbucket, Jira, PostgreSQL and Nginx servers. (docker)

With default configuration:

* Jira on http://localhost:8080/JIRA - over Nginx reverse proxy
* Bitbucket on http://localhost:7990/Bitbucket - over Nginx reverse proxy
* PostgreSQL on http://localhost:5432

#### Prerequisites

Docker & Docker Compose Python 3.x (request package)

#### Getting Started To Run Jira/Bitbucket

Clone this repository.

```bash
git clone --recursive https://github.com/TheNavyInfantry/devops-task.git
cd devops-task
```

Run docker-compose

```bash
docker-compose up
```

Then install Jira and Bitbucket. Use PostgreSQL with these credentials: for Jira use `jiradb`, for bitbucket
use `bitbucket` username: `root` password: `root`

#### Getting Started To Run Script

Install requests package:

```bash
pip install requests
```

Run the scripts:

```bash
python script.py
```

## Troubleshooting

You may would like to cleanup your containers and volumes when you get stucked. At that time use this
script: `cleanup.sh`

## Known issues

* Integration between Jira and Bitbucket does not work due to host resolve and reverse proxy (help wanted) (Jira and
  Bitbucket rejects connection on non-proxy connections)

## Contributing

Merge requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details