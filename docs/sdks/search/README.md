# Search
(*search*)

## Overview

### Available Operations

* [list_search_results](#list_search_results) - List Search Results
* [count_search_results](#count_search_results) - Show Results Count
* [export_search_results](#export_search_results) - Export Search Results

## list_search_results

Returns the search results. See [Query basics](#query-basics) for the syntax of the `query` parameter.

Use the ampersand character (&) to append the `sort_by` or `sort_order` parameters to the URL.

For examples, see [Searching with Zendesk API](/documentation/ticketing/using-the-zendesk-api/searching-with-the-zendesk-api).

#### Allowed For

* Agents

#### Pagination

* Offset pagination only

Offset pagination may result in duplicate results when paging. You can also use the
[Export Search Results](/api-reference/ticketing/ticket-management/search/#export-search-results) endpoint, which
uses cursor-based pagination and doesn't return duplicate results. See
[Using cursor pagination](/api-reference/introduction/pagination/#using-cursor-pagination) for more information.


#### Errors JSON Format

Errors are represented as JSON objects which have the following keys:

| Name                  | Type                 | Comment
| --------------------- | ---------------------| --------------------
| error                 | string               | The type of error. Examples: "unavailable", "invalid"
| description           | string               |

##### Example Error
```js
{
  "error": "unavailable",
  "description": "Sorry, we could not complete your search query. Please try again in a moment."
}
```


### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.search.list_search_results(query="https://subdomain.zendesk.com/api/v2/search.json?query=type:ticket status:closed&sort_by=status&sort_order=desc", page=1, per_page=100)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                                                                       | Type                                                                                                                                                                                            | Required                                                                                                                                                                                        | Description                                                                                                                                                                                     | Example                                                                                                                                                                                         |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `query`                                                                                                                                                                                         | *str*                                                                                                                                                                                           | :heavy_check_mark:                                                                                                                                                                              | The search query. See [Query basics](#query-basics) above. For details on the query syntax, see the [Zendesk Support search reference](https://support.zendesk.com/hc/en-us/articles/203663226) | https://subdomain.zendesk.com/api/v2/search.json?query=type:ticket status:closed&sort_by=status&sort_order=desc                                                                                 |
| `sort_by`                                                                                                                                                                                       | [Optional[models.SortBy]](../../models/sortby.md)                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                              | One of `updated_at`, `created_at`, `priority`, `status`, or `ticket_type`. Defaults to sorting by relevance                                                                                     |                                                                                                                                                                                                 |
| `sort_order`                                                                                                                                                                                    | [Optional[models.SortOrder]](../../models/sortorder.md)                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                              | One of `asc` or `desc`.  Defaults to `desc`                                                                                                                                                     |                                                                                                                                                                                                 |
| `page`                                                                                                                                                                                          | *Optional[int]*                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                              | Page number for offset pagination                                                                                                                                                               |                                                                                                                                                                                                 |
| `per_page`                                                                                                                                                                                      | *Optional[int]*                                                                                                                                                                                 | :heavy_minus_sign:                                                                                                                                                                              | Number of items per page                                                                                                                                                                        |                                                                                                                                                                                                 |
| `retries`                                                                                                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                | :heavy_minus_sign:                                                                                                                                                                              | Configuration to override the default retry behavior of the client.                                                                                                                             |                                                                                                                                                                                                 |

### Response

**[models.ListSearchResultsResponse](../../models/listsearchresultsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## count_search_results

Returns the number of items matching the query rather than the items. The search string works the same as a regular search.

#### Allowed For

- Agents


### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.search.count_search_results(query="https://subdomain.zendesk.com/api/v2/search.json?query=type:ticket status:closed")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      | Example                                                                          |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `query`                                                                          | *str*                                                                            | :heavy_check_mark:                                                               | The search query                                                                 | https://subdomain.zendesk.com/api/v2/search.json?query=type:ticket status:closed |
| `retries`                                                                        | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                 | :heavy_minus_sign:                                                               | Configuration to override the default retry behavior of the client.              |                                                                                  |

### Response

**[models.SearchCountResponse](../../models/searchcountresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## export_search_results

Exports a set of results. See [Query syntax](#query-syntax) for the syntax of the `query` parameter.

Use this endpoint for search queries that will return more than 1000 results. The result set is ordered only by the `created_at` attribute.

The search only returns results of a single object type. The following object types are supported: ticket, organization, user, or group.

You must specify the type in the `filter[type]` parameter. Searches with type in the query string will result in an error.

#### Allowed For

- Agents

#### Pagination

- Cursor pagination

See [Pagination](/api-reference/introduction/pagination/).

Returns a maximum of 1000 records per page. The number of results shown in a page is determined by the `page[size]` parameter.

**Note**: You may experience a speed reduction or a timeout if you request 1000 results per page and you have many archived tickets in the results. Try reducing the number of results per page. We recommend 100 results per page.

The cursor specified by the `after_cursor` property in a response expires after one hour.

For more information on cursor-based pagination, see the following articles:

- [Comparing cursor pagination and offset pagination](/documentation/developer-tools/pagination/comparing-cursor-pagination-and-offset-pagination)
- [Paginating through lists using cursor pagination](/documentation/developer-tools/pagination/paginating-through-lists-using-cursor-pagination)

#### Limits

This API endpoint is rate-limited to 100 requests per minute per account. The limit also counts towards the global API rate limit.

#### Response Format

| Name                  | Type                 | Comment
| --------------------- | ---------------------| --------------------
| links[next]           | string               | URL to the next page of results
| meta[has_more]        | string               | Boolean indicating if there are more results
| meta[after_cursor]    | string               | Cursor object returned from the Search Service
| results               | array                | May consist of tickets, users, groups, or organizations, as specified by the `filter_type` parameter

The response is similar to the response of `GET /api/v2/search.json?`, with a few changes:

* `links` - Has the following nested properties: `prev` and `next`. These replace the `next_page` and `prev_page` links. The `prev` property is always null because backward pagination is not supported. The `next` property may include an auto-generated link to the next page of results.
* `meta` - Has the following nested properties: `has_more` and `after_cursor`. The `has_more` property indicates whether the next page has more results. The `after_cursor` property is the cursor used to paginate to the next page. It expires after one hour.

There's no `count` property.


### Example Usage

```python
from zendesk import Zendesk, models


with Zendesk(
    security=models.Security(
        username="",
        password="",
    ),
) as z_client:

    res = z_client.search.export_search_results(query="https://subdomain.zendesk.com/api/v2/search.json?query=type:ticket status:closed&sort_by=status&sort_order=desc", page_size=100)

    while res is not None:
        # Handle items

        res = res.next()

```

### Parameters

| Parameter                                                                                                                                                                                                                                                                                                           | Type                                                                                                                                                                                                                                                                                                                | Required                                                                                                                                                                                                                                                                                                            | Description                                                                                                                                                                                                                                                                                                         | Example                                                                                                                                                                                                                                                                                                             |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `query`                                                                                                                                                                                                                                                                                                             | *str*                                                                                                                                                                                                                                                                                                               | :heavy_check_mark:                                                                                                                                                                                                                                                                                                  | The search query. See [Query basics](#query-basics) above. For details on the query syntax, see the [Zendesk Support search reference](https://support.zendesk.com/hc/en-us/articles/203663226)                                                                                                                     | https://subdomain.zendesk.com/api/v2/search.json?query=type:ticket status:closed&sort_by=status&sort_order=desc                                                                                                                                                                                                     |
| `page_before`                                                                                                                                                                                                                                                                                                       | *Optional[str]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | A [pagination cursor](/documentation/api-basics/pagination/paginating-through-lists-using-cursor-pagination) that tells the endpoint which page to start on. It should be a `meta.before_cursor` value from a previous request. Note: `page[before]` and `page[after]` can't be used together in the same request.<br/> |                                                                                                                                                                                                                                                                                                                     |
| `page_after`                                                                                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | A [pagination cursor](/documentation/api-basics/pagination/paginating-through-lists-using-cursor-pagination) that tells the endpoint which page to start on. It should be a `meta.after_cursor` value from a previous request. Note: `page[before]` and `page[after]` can't be used together in the same request.<br/> |                                                                                                                                                                                                                                                                                                                     |
| `page_size`                                                                                                                                                                                                                                                                                                         | *Optional[int]*                                                                                                                                                                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Specifies how many records should be returned in the response. You can specify up to 100 records per page.<br/>                                                                                                                                                                                                     |                                                                                                                                                                                                                                                                                                                     |
| `filter_type`                                                                                                                                                                                                                                                                                                       | [Optional[models.FilterType]](../../models/filtertype.md)                                                                                                                                                                                                                                                           | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | The object type returned by the export query. Can be `ticket`, `organization`, `user`, or `group`.                                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                     |
| `retries`                                                                                                                                                                                                                                                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                  | Configuration to override the default retry behavior of the client.                                                                                                                                                                                                                                                 |                                                                                                                                                                                                                                                                                                                     |

### Response

**[models.ExportSearchResultsResponse](../../models/exportsearchresultsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |