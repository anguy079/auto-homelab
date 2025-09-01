Go to https://github.com/{{ GH_USERNAME }}/{{ FORK_NAME }}/settings  
Click **Leave fork network**  
Then run:
```bash
git clone https://github.com/{{ GH_USERNAME }}/{{ FORK_NAME }}.git && \
cd {{ FORK_NAME }} && \
git remote add upstream https://github.com/{{ REPO_ORIGIN }}.git && \
git remote -v
```
