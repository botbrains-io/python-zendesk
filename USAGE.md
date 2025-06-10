<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.assignee_field_assignable_groups.list_assignee_field_assignable_groups_and_agents_search(name="Johnny Agent")

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from zendesk import Zendesk, models

async def main():

    async with Zendesk(
        security=models.Security(
            username="",
            password="",
        ),
    ) as z_client:

        res = await z_client.assignee_field_assignable_groups.list_assignee_field_assignable_groups_and_agents_search_async(name="Johnny Agent")

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->