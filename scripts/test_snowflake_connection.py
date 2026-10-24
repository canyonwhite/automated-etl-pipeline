from retail_pipeline.warehouse import (
    create_snowflake_connection,
)


def main():
    connection = create_snowflake_connection()

    try:
        cursor = connection.cursor()

        try:
            cursor.execute("""
                SELECT
                    CURRENT_DATABASE(),
                    CURRENT_SCHEMA(),
                    CURRENT_ROLE()
            """)

            print(cursor.fetchone())

        finally:
            cursor.close()

    finally:
        connection.close()


if __name__ == "__main__":
    main()