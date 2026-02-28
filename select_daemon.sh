#!/bin/bash

# Cowboy Elemental Simulation Workflow
# Generates a random daemon document with simulated user archetype

DAEMONS=("arboriel" "ferrosid" "jvalion" "humavita" "aerunik" "sentaria" "nema")
THEMES=("nature" "technology" "chaos" "order" "void" "light" "shadow" "time" "space" "mind")

daemon=${DAEMONS[$RANDOM % ${#DAEMONS[@]}]}
theme=${THEMES[$RANDOM % ${#THEMES[@]}]}

# Generate topic based on daemon
case $daemon in
    arboriel) topic="forest ecosystem restoration" ;;
    ferrosid) topic="metallurgical innovation" ;;
    jvalion) topic="volcanic energy systems" ;;
    humavita) topic="community resilience networks" ;;
    aerunik) topic="atmospheric current patterns" ;;
    sentaria) topic="consciousness expansion methods" ;;
    nema) topic="interdimensional harmonics" ;;
esac

echo "$daemon|$theme|$topic"
