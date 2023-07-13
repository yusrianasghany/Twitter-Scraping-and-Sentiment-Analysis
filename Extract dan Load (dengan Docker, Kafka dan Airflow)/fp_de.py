from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from includes.vs_modules.test import hello
import includes.vs_modules.Consumer as Consumer
import includes.vs_modules.Producer as Producer

args = {
    'owner': 'Yusrian Asghany',
    'start_date': days_ago(1) # make start date in the past
}

dag = DAG(
    dag_id='fp_de',
    default_args=args,
    schedule_interval='@daily' # make this workflow happen every day
)

with dag:
    consumer = PythonOperator(
        task_id='producer',
        python_callable=Producer.task,
    )
    producer = PythonOperator(
        task_id='consumer',
        python_callable=Consumer.task,
    )