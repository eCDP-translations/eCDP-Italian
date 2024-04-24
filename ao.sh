#!/bin/bash

# Funzione per trasformare il file JSON e aggiungere il commento
transform_json() {
    local file="$1"
    local temp_file=$(mktemp)

    # Trasforma l'array JSON in oggetto JSON
    jq 'to_entries | map({key: (.key | tostring), value: .value}) | from_entries' "$file" >> "$temp_file"

    echo "File $file trasformato con successo."
}

# Trova tutti i file JSON in modo ricorsivo e applica la trasformazione solo se iniziano con un array
find . -type f -name "*.json" | while read file; do
    # Controlla se il file non è vuoto
    if [ -s "$file" ]; then
        # Controlla se il file inizia con [
        if [ "$(head -c 1 "$file")" = "[" ]; then
            transform_json "$file"
        else
            echo "Il file $file non inizia con un array, trasformazione non applicata."
        fi
    else
        echo "Attenzione: Il file $file è vuoto."
    fi
done
