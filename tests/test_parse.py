#!/usr/bin/env python3
import org_todo_send.parse as parse
import logging

def test_get_todos_for_recipient():
    todos = parse.get_todos_from_org("tests/test.org")
    recipient = "alice"
    df = parse.get_todos_for_recipient(todos, recipient)
    logging.info(list(df["people"]))
    assert recipient in df["people"].sum()
    assert "everyone" in df["people"].sum()

def test_format_message():
    todos = parse.get_todos_from_org("tests/test.org")
    recipient = "alice"
    message = parse.format_message("TODOs", recipient, todos)

    logging.info(message)
    assert "TODOs" in message
    assert "Project 1" in message
    assert "Project 2" in message
    assert "- Todo1 [Deadline: Tue 7/23/24]" in message
    assert "- Todo3" in message
