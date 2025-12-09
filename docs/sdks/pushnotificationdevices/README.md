# PushNotificationDevices

## Overview

### Available Operations

* [push_notification_devices](#push_notification_devices) - Bulk Unregister Push Notification Devices

## push_notification_devices

Unregisters the mobile devices that are receiving push notifications. Specify the devices as an array of mobile device tokens.

#### Allowed for

* Admins

### Example Usage

<!-- UsageSnippet language="python" operationID="PushNotificationDevices" method="post" path="/api/v2/push_notification_devices/destroy_many" -->
```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.push_notification_devices.push_notification_devices(request={
        "push_notification_devices": [
            "token1",
            "token2",
        ],
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                               | Type                                                                                    | Required                                                                                | Description                                                                             |
| --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `request`                                                                               | [models.PushNotificationDevicesRequest](../../models/pushnotificationdevicesrequest.md) | :heavy_check_mark:                                                                      | The request object to use for the request.                                              |
| `retries`                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                        | :heavy_minus_sign:                                                                      | Configuration to override the default retry behavior of the client.                     |

### Response

**[str](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |