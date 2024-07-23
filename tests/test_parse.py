#!/usr/bin/env python3
import org_todo_send.parse as parse

def test_get_todos_for_recipient_everyone():
    todos = parse.get_todos_from_org("tests/test.org")
    recipient = "alice"
    df = parse.get_todos_for_recipient(todos, recipient)
    df.to_csv("tests/test_get_todos_for_recipient.csv")

    assert recipient in df["people"].sum()
    assert "everyone" in df["people"].sum()
