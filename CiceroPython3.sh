#!/bin/bash

# Name:    CiceroCloudAPI
# Purpose: Execute the CiceroCloudAPI program

######################### Constants ##########################

RED='\033[0;31m' #RED
NC='\033[0m' # No Color

######################### Parameters ##########################

lat=""
long=""
location=""
license=""
max=""

while [ $# -gt 0 ] ; do
  case $1 in
    --lat)
        if [ -z "$2" ] || [[ $2 =~ ^--?[a-zA-Z]+$ ]];
        then
            printf "${RED}Error: Missing an argument for parameter 'lat'.${NC}\n"
            exit 1
        fi
        lat="$2"
        shift
        ;;
    --long)
        if [ -z "$2" ] || [[ $2 =~ ^--?[a-zA-Z]+$ ]];
        then
            printf "${RED}Error: Missing an argument for parameter 'long'.${NC}\n"
            exit 1
        fi
        long="$2"
        shift
        ;;
    --location)
        if [ -z "$2" ] || [[ $2 =~ ^--?[a-zA-Z]+$ ]];
        then
            printf "${RED}Error: Missing an argument for parameter 'location'.${NC}\n"
            exit 1
        fi
        location="$2"
        shift
        ;;
    --max)
        if [ -z "$2" ] || [[ $2 =~ ^--?[a-zA-Z]+$ ]];
        then
            printf "${RED}Error: Missing an argument for parameter 'max'.${NC}\n"
            exit 1
        fi
        max="$2"
        shift
        ;;
    --license)
        if [ -z "$2" ] || [[ $2 =~ ^--?[a-zA-Z]+$ ]];
        then
            printf "${RED}Error: Missing an argument for parameter 'license'.${NC}\n"
            exit 1
        fi
        license="$2"
        shift
        ;;
  esac
  shift
done

########################## Main ############################
printf "\n=================================== Melissa Cicero Cloud API =====================================\n"

# Get license (either from parameters or user input)
if [ -z "$license" ];
then
  printf "Please enter your license string: "
  read license
fi

# Check for License from Environment Variables 
if [ -z "$license" ];
then
  license=`echo $MD_LICENSE` 
fi

if [ -z "$license" ];
then
  printf "\nLicense String is invalid!\n"
  exit 1
fi

# Run project
if [ -z "$lat" ] && [ -z "$long" ];
then
    python3 CiceroPython3.py --license $license 
else
    python3 CiceroPython3.py --license $license --lat "$lat" --long "$long" --location "$location" --max "$max"
fi

