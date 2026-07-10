from bytrace_app.db import get_connection


def save_event(
    event_type,
    converter_type=None,
    input_value=None,
    output_value=None,
    clicked_element=None,
    previous_page_url=None,
    target_page_url=None,
    status="success",
    user_ip=None,
    user_agent=None
):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO events (
            event_type,
            converter_type,
            input_value,
            output_value,
            clicked_element,
            previous_page_url,
            target_page_url,
            status,
            user_ip,
            user_agent
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """,
        (
            event_type,
            converter_type,
            input_value,
            output_value,
            clicked_element,
            previous_page_url,
            target_page_url,
            status,
            user_ip,
            user_agent
        )
    )

    connection.commit()
    cursor.close()
    connection.close()