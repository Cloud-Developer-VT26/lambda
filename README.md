# Lambda

För att driftsätta kod till en Lambda-funktion lokalt med AWS CLI så skapa först en zip-fil med er kod (Obs! Enbart filerna inte någon mapp). Därefter skriv följande kommando i terminalen och ersätt funktionsnamn och zipfils-namn med era namn.

```bash
aws lambda update-function-code --function-name lambda-funktion-namn --zip-file fileb://namn-på-zip-fil.zip
```

Du behöver sedan skapa en funktions url till din lambda för att kunna trigga den. Detta kan du göra i AWS på din Lambda - funktion och välja Configuration och sedan Function URL och sedan välj Create Function URL. Välj NONE som Auth Type.
