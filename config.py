# This file is for any configuration option that can define how the bot behaves on certain events or situations.

AUTOLEAVE_UNTRUSTED_SERVERS = False
# auto-leaves any server that is not MAIN or STAFF on any event

CONST_DEVELOPERS_MAXPERM_DEBUG = True
# if True, users hardcoded in src/cnst.py::developers_uid will bypass all broad type permission checks.
# this is strictly for testing purposes, and should be set to False when in large production use or not patching/testing

ARE_ACTIONS_AUDITED = True
# if True, all actions that require a certain permission tier (DEVreq excluded) will be logged in
# the database-backed audit log, visible with slash commands to all staff