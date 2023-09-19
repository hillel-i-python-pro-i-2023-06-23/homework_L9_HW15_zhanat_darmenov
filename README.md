# homework_L9_HW15_zhanat_darmenov


# Flask application  L9 HW15

---
![Main workflow](https://github.com/hillel-i-python-pro-i-2023-06-23/homework_L9_HW15_zhanat_darmenov/actions/workflows/main-workflow.yml/badge.svg)

## 🏠 Homework

Homework related actions.

### ▶️ Run

Make all actions needed for run homework from zero. Including configuration.

```shell
make d-homework-i-run
```

### 🚮 Purge

Make all actions needed for run homework from zero.

```shell
make d-homework-i-purge
```

---

## 🛠️ Dev

### Initialize dev

Install dependencies and register pre-commit.

```shell
make init-dev
```

### ⚙️ Configure

Configure homework.

```shell
make init-configs
```

---

## 🐳 Docker

Use services in dockers.

### ▶️ Run

Just run

```shell
make d-run
```

### ⏹️Stop

Stop services

```shell
make d-stop
```


---

Base page:
"http://127.0.0.1:48000" 
or
"http://127.0.0.1:48000/hello/"


Return User info via query route:
"http://127.0.0.1:48000/query/<string:name>/<int:numb>/"


Return User from DB. If it is not there - Add it to DB.
"http://127.0.0.1:48000/database/<string:name>/<int:numb>/"
