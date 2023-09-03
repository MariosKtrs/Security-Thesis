#!/bin/bash

encrypt() {
    local input="$1"
    local key="$2"
    local encrypted=""

    for ((i = 0; i < ${#input}; i++)); do
        input_char="${input:i:1}"
        key_char="${key:i % ${#key}:1}"
        encrypted_char=$(( (input_char ^ key_char) + 32 ))
         encrypted+=$(printf "\\$(printf '%03o' "$encrypted_char")")
    done

    echo "$encrypted"
}

decrypt() {
    local input="$1"
    local key="$2"
    local decrypted=""

    for ((i = 0; i < ${#input}; i += 3)); do
        input_chunk="${input:i:3}"
        decrypted_char=$(( 8#"$input_chunk" ^ $(printf '%d' "'$key'") - 32 ))
        decrypted+=$(printf "\\$(printf '%03o' "$decrypted_char")")
    done

    echo "$decrypted"
}

case "$1" in
    encrypt)
        encrypted=$(encrypt "$3" "$2")
        echo "Encrypted data: $encrypted"
        ;;
    decrypt)
        decrypted=$(decrypt "$3" "$2")
        echo "Decrypted data: $decrypted"
        ;;
    *)
        echo "Usage: <encrypt|decrypt> <key> <data>"
        exit 1
        ;;
esac
