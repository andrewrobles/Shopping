# How to set up the app
- Make sure that Python and Node are installed
- Run the following commands in the `api` directory:
```bash
cd api
python3 -m venv venv
pip install -r requirements.txt
python3 manage.py migrate
python3 manage.py test
python3 manage.py runserver
```
- Run the following commands in the `client` directory:
```bash
cd client
npm install
npm run dev
```

# How to run tests
- API tests
```
cd api
python3 -m venv venv
python3 manage.py test
```
- Client tests (make sure api is running)
```
cd client
npm run cypress
```

Contact `Andrew Robles` if you have any issues at `andrewrobles@berkeley.edu` I am very responsive

