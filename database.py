from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STR']


# Buluttaki mysql veri tablosuna bağlanıyoruz.
engine = create_engine(
    db_connection_string,
    connect_args={
        'ssl': {
            # PLanetScale.com'da oluşturduğum veri tabanının güvenlik ayarlarında verdiği sslcs ayarı aşağıda. Güvenli bağlantı için gerekli.
            "sslca": "/etc/ssl/cert.pem"
        }
    })


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(row._asdict())
    return jobs
