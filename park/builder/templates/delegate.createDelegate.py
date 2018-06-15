var ark = require("{{ javascript }}");

ark.crypto.setNetworkVersion({{ network }});

var transaction = ark.delegate.createDelegate(
    "{{ secret }}",
    "{{ username }}",
    {% if secondSecret %}
        "{{ secondSecret }}"
    {% endif %}
);

console.log(JSON.stringify(transaction));
