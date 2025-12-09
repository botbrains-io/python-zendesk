speakeasy run
find src/zendesk -type f -name "*.py" ! -name "enums.py" -exec sed -i '' 's/type=type,/type_=type_,/g' {} +