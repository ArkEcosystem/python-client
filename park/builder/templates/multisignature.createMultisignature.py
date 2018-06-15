var ark = require("{{ javascript }}");

ark.crypto.setNetworkVersion({{ network }});

var transaction = ark.multisignature.createMultisignature(
    "{{ secret }}",
    {% if secondSecret %}
        "{{ secondSecret }}",
    {% endif %}
    "{{ keysgroup }}",
    "{{ lifetime }}",
    "{{ min }}",
);

console.log(JSON.stringify(transaction));
