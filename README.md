# pull-dashboard

For this to run, you will need a Github access key in your environment, called GITHUB_API_KEY. All it needs is Land registry public repos read access.

## Running

```bash
sudo pip install -r requirements.txt
export GITHUB_API_KEY=<key>
./run_flask_dev.py
```

## Configuration

The list of repositories to exclude are in held in the file pointed to by the config.py::BLACKLIST_REPOSITORIES entry. Currently this is 'Blacklistfile'.

