# Quart-GraphQL

Adds GraphQL support to your Quart application.

## Usage

Just use the `AsyncGraphQLView` view from `quart_graphql`

```python
from quart_graphql import AsyncGraphQLView

app.add_url_rule('/graphql', view_func=AsyncGraphQLView.as_view('graphql', schema=schema, graphiql=True))

# Optional, for adding batch query support (used in Apollo-Client)
app.add_url_rule('/graphql/batch', view_func=AsyncGraphQLView.as_view('graphql', schema=schema, batch=True))
```

This will add `/graphql` and `/graphiql` endpoints to your app.

### Supported options
 * `schema`: The `GraphQLSchema` object that you want the view to execute when it gets a valid request.
 * `context`: A value to pass as the `context` to the `graphql()` function.
 * `root_value`: The `root_value` you want to provide to `executor.execute`.
 * `pretty`: Whether or not you want the response to be pretty printed JSON.
 * `executor`: The `Executor` that you want to use to execute queries.
 * `graphiql`: If `True`, may present [GraphiQL](https://github.com/graphql/graphiql) when loaded directly from a browser (a useful tool for debugging and exploration).
 * `graphiql_template`: Inject a Jinja template string to customize GraphiQL.
 * `batch`: Set the GraphQL view as batch (for using in [Apollo-Client](http://dev.apollodata.com/core/network.html#query-batching) or [ReactRelayNetworkLayer](https://github.com/nodkz/react-relay-network-layer))
 * `middleware`: A list of graphql [middlewares](http://docs.graphene-python.org/en/latest/execution/middleware/).

You can also subclass `AsyncGraphQLView` and overwrite `get_root_value(self, request)` to have a dynamic root value
per request.

```python
class UserRootValue(AsyncGraphQLView):
    def get_root_value(self, request):
        return request.user

```
