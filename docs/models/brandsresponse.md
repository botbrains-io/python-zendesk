# BrandsResponse


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `count`                                              | *Optional[int]*                                      | :heavy_minus_sign:                                   | the total record count                               |
| `next_page`                                          | *OptionalNullable[str]*                              | :heavy_minus_sign:                                   | the URL of the next page                             |
| `previous_page`                                      | *OptionalNullable[str]*                              | :heavy_minus_sign:                                   | the URL of the previous page                         |
| `brands`                                             | List[[models.BrandObject](../models/brandobject.md)] | :heavy_minus_sign:                                   | Array of brands                                      |