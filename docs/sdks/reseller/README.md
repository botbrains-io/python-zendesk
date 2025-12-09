# Reseller

## Overview

### Available Operations

* [create_trial_account](#create_trial_account) - Create Trial Account
* [verify_subdomain_availability](#verify_subdomain_availability) - Verify Subdomain Availability

## create_trial_account

Create Trial Account

### Example Usage

<!-- UsageSnippet language="python" operationID="CreateTrialAccount" method="post" path="/api/v2/accounts" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.reseller.create_trial_account()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.TrialAccountResponse](../../models/trialaccountresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## verify_subdomain_availability

Zendesk Support credentials are not required to access this endpoint. You can use any Zendesk Support subdomain.

Returns "true" if the subdomain is available.


### Example Usage

<!-- UsageSnippet language="python" operationID="VerifySubdomainAvailability" method="get" path="/api/v2/accounts/available" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.reseller.verify_subdomain_availability(subdomain="z3ndesk")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                      | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `subdomain`                                                                                                    | *str*                                                                                                          | :heavy_check_mark:                                                                                             | Specify the name of the subdomain you want to verify. The name can't contain underscores, hyphens, or spaces.<br/> |
| `retries`                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                               | :heavy_minus_sign:                                                                                             | Configuration to override the default retry behavior of the client.                                            |

### Response

**[models.VerifySubdomainAvailabilityResponse](../../models/verifysubdomainavailabilityresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |