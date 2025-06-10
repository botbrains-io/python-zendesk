# ConditionsObject

An object that describes the conditions under which the automation will execute. See [Conditions reference](/documentation/ticketing/reference-guides/conditions-reference)


## Fields

| Field                                                                             | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `all`                                                                             | List[[models.ConditionObject](../models/conditionobject.md)]                      | :heavy_minus_sign:                                                                | Logical AND. Tickets must fulfill all of the conditions to be considered matching |
| `any`                                                                             | List[[models.ConditionObject](../models/conditionobject.md)]                      | :heavy_minus_sign:                                                                | Logical OR. Tickets may satisfy any of the conditions to be considered matching   |