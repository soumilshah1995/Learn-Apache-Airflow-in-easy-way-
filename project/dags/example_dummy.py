from airflow import DAG
from airflow.utils.dates import days_ago

try:
	from airflow.operators.python import PythonOperator
except ImportError:
	from airflow.operators.python_operator import PythonOperator

import time
import requests
import random


args = {
	"owner": "pratik"
}


def random_failure():
	v = random.randint(0,100)
	thresh = 95

	if v <= thresh:
		return v

	raise ValueError(f"random value {v} greater than {thresh}")

def fail():
	raise ValueError("Failed on purpose")

with DAG(
	dag_id="example_dummy",
	default_args=args,
	start_date=days_ago(2),
	tags=['example']) as dag:

	task1 = PythonOperator(task_id="task-1", python_callable=random_failure)
	task2 = PythonOperator(task_id="task-2", python_callable=random_failure)
	task3 = PythonOperator(task_id="task-3", python_callable=random_failure)
	task4 = PythonOperator(task_id="task-4", python_callable=random_failure)
	task5 = PythonOperator(task_id="task-5", python_callable=random_failure)
	# task6 = PythonOperator(task_id="task-6", python_callable=random_failure)
	task6 = PythonOperator(task_id="task-6", python_callable=fail)
	task7 = PythonOperator(task_id="task-7", python_callable=random_failure)

	task1 >> [task2, task3]
	task3 >> [task4, task5]
	task2 >> task6
	task6 >> task7




