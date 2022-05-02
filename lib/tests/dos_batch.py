"""Batch tests."""
from lib.utils import graph_query, curlify


def batch_query(url, proxy, headers):
  """Check for batch queries."""
  res = {
    'result':False,
    'title':'Array-based Query Batching',
    'description':'Batch queries allowed with 10+ simultaneous queries',
    'impact':'Denial of Service',
    'severity':'HIGH',
    'curl_verify':''
  }

  gql_response = graph_query(url, proxies=proxy, headers=headers, payload='query { __typename }', batch=True)
  
  res['curl_verify'] = curlify(gql_response)
  
  try:
      if len(gql_response.json()) >= 10:
        res['result'] = True
  except:
    pass

  return res
