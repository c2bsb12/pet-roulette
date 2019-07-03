# Pet-Roulette

Pet-Roulette is a application which allows the user to pull information about a randomly generated adoptable pet within the vicinity of a selected zipcode

##Attributes
-Data was accessed through the Pet Finder API https://www.petfinder.com/developers/.
-Some of the code was also constructed using set up instructions on the API website.
-The README file was constructed using examples from past projects in Professor Rossetti's Python Programming & Software Development class to inform structure.
-Some input was received from family friend, Waldo Bronchart, on how to use the random module.


## Prerequisites

  + Anaconda 3.7
  + Python 3.7
  + Pip

  NOTE: Pet finder API can be requested at https://www.petfinder.com/developers/. The user will be asked to register for an account to create an application. 
  
  When requesting an API key, the user will also receive an "access token", which expires every 36 minutes. To [obtain a new access token], the user must enter the following prompt in a new terminal window, replacing the `{PETFINDER_API_KEY}` and `{PETFINDER_CLIENT_SECRET}` with the user's credentials (removing the curly braces)

```sh
curl -d "grant_type=client_credentials&client_id={PETFINDER_API_KEY}&client_secret={PETFINDER_CLIENT_SECRET}" https://api.petfinder.com/v2/oauth2/token
```

The output will resemble the following

```
{
    "token_type":"Bearer",
    "expires_in":3600,
    "access_token":"somelongstring-xyz"
}

The user can then add a file called ".env" and store the access token (e.g. somelongstring-xyz)  in an environment variable called `PETFINDER_ACCESS_TOKEN`. This token will need to be replaced every 36 minutes. 

##Installation

Fork the repository from [GitHub source]https://github.com/c2bsb12/get_a_pet.

Then use GitHub Desktop or the command-line to "clone" or download your fork onto your local computer:

```sh
git clone https://github.com/YOUR_USERNAME/get_a_pet.

Navigate into your local repo from the command-line before running any of the other commands below:

```sh
cd get_a_pet
```


## Setup

Create and activate a new Anaconda virtual environment:

```sh
conda create -n pets-env-7 python=3.7
conda activate pets-env-7
```


Install Python package dependencies:

```sh
pip install requests 
```

```sh
pip install python-dotenv
```

## Usage

Run the app using the following command:

```sh
python pets.py
```