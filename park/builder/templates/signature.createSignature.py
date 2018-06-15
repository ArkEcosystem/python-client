var ark = require("{{ javascript }}");

ark.crypto.setNetworkVersion({{ network }});

var transaction = ark.signature.createSignature(
    "{{ secret }}",

    {% if secondSecret %}
        "{{ secondSecret }}"
    {% endif %}
);

console.log(JSON.stringify(transaction));
