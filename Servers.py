import discord
import asyncio


def server_count(client):
    return len(client.servers)


def server_list(client):
    return client.servers


def server_name_list(client):
    server_names = []
    for server in client.servers:
        server_names.append(str(server))
    return server_names
