#!/bin/bash
exec hypercorn api.api:app -b 0.0.0.0:80 --worker-class trio
