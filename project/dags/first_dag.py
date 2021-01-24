try:

    from datetime import timedelta
    from airflow import DAG
    from airflow.operators.python_operator import PythonOperator
    from datetime import datetime
    import pandas as pd

    print("All Dag modules are ok ......")
except Exception as e:
    print("Error  {} ".format(e))


def first_function_execute(**context):
    print("first_function_execute   ")
    context['ti'].xcom_push(key='mykey', value="first_function_execute says Hello ")


def second_function_execute(**context):
    instance = context.get("ti").xcom_pull(key="mykey")
    data = [{"name":"Soumil","title":"Full Stack Software Engineer"}, { "name":"Nitin","title":"Full Stack Software Engineer"},]
    df = pd.DataFrame(data=data)
    print('@'*66)
    print(df.head())
    print('@'*66)

    print("I am in second_function_execute got value :{} from Function 1  ".format(instance))


with DAG(
        dag_id="first_dag",
        schedule_interval="@daily",
        default_args={
            "owner": "airflow",
            "retries": 1,
            "retry_delay": timedelta(minutes=5),
            "start_date": datetime(2021, 1, 1),
        },
        catchup=False) as f:

    first_function_execute = PythonOperator(
        task_id="first_function_execute",
        python_callable=first_function_execute,
        provide_context=True,
        op_kwargs={"name":"Soumil Shah"}
    )

    second_function_execute = PythonOperator(
        task_id="second_function_execute",
        python_callable=second_function_execute,
        provide_context=True,
    )

first_function_execute >> second_function_execute


