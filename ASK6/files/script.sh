#!/bin/bash

vuln_encr() {
    local input=$(cat "$2")
    local key="$3"
    local encrypted=""

     for ((i=0; i<${#input}; i++)); do
        key_char="${key:i % ${#key}:1}"
        input_char="${input:i:1}"
        encrypted_char=$(( (input_char ^ key_char) + 32 ))
        encrypted+=$(printf "\\$(printf '%03o' "$encrypted_char")")
    done

    echo "$encrypted" > mitsos.txt
}

vuln_decr() {
    local input=$(cat "$2")
    local key="$3"
    local decrypted=""

    for ((i=0; i < ${#input}; i+=3)); do
        input_chunk="${input:i:3}"
        decrypted_char=$(( 8#"$input_chunk" ^ $(printf '%d' "'$key'") - 32 ))
        decrypted+=$(printf "\\$(printf '%03o' "$decrypted_char")")
    done

    echo "$decrypted"
}

format() {
    echo "Usage: <encrypt|decrypt> <filename> <key>"
    exit 1
}

case "$1" in
    encrypt)
        encrypted=$(vuln_encr "$1" "$2" "$3")
        echo "Encrypted data: $encrypted"
        ;;
    decrypt)
        decrypted=$(vuln_decr "$1" "$2" "$3")
        echo "Decrypted data: $decrypted"
        ;;
    *)
        format
        ;;
esac
