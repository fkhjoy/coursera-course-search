import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:104.0) Gecko/20100101 Firefox/104.0',
    'Host': 'lua9b20g37-dsn.algolia.net',
    'Origin': 'https://www.coursera.org',
    'Referer': 'https://www.coursera.org/',
}

payload = {"requests":[{"indexName":"DO_NOT_DELETE_PLACEHOLDER_INDEX_NAME","params":"query=graphics%20design&page=0&highlightPreTag=%3Cais-highlight-0000000000%3E&highlightPostTag=%3C%2Fais-highlight-0000000000%3E&clickAnalytics=true&facets=%5B%5D&tagFilters="},{"indexName":"prod_all_launched_products_term_optimization_skills_test_for_precise_xdp_imprecise_variant","params":"query=graphics%20design&hitsPerPage=12&maxValuesPerFacet=1000&page=1&highlightPreTag=%3Cais-highlight-0000000000%3E&highlightPostTag=%3C%2Fais-highlight-0000000000%3E&clickAnalytics=true&facets=%5B%22isCreditEligible%22%2C%22topic%22%2C%22skills%22%2C%22productDifficultyLevel%22%2C%22productDurationEnum%22%2C%22entityTypeDescription%22%2C%22partners%22%2C%22allLanguages%22%5D&tagFilters="},{"indexName":"prod_degrees","params":"query=data%20science&hitsPerPage=10&maxValuesPerFacet=1000&page=0&highlightPreTag=%3Cais-highlight-0000000000%3E&highlightPostTag=%3C%2Fais-highlight-0000000000%3E&clickAnalytics=true&facets=%5B%22isCreditEligible%22%2C%22topic%22%2C%22skills%22%2C%22productDifficultyLevel%22%2C%22productDurationEnum%22%2C%22entityTypeDescription%22%2C%22partners%22%2C%22allLanguages%22%5D&tagFilters="},{"indexName":"test_suggestions","params":"query=data%20science&hitsPerPage=10&maxValuesPerFacet=1000&page=0&highlightPreTag=%3Cais-highlight-0000000000%3E&highlightPostTag=%3C%2Fais-highlight-0000000000%3E&clickAnalytics=true&facets=%5B%22isCreditEligible%22%2C%22topic%22%2C%22skills%22%2C%22productDifficultyLevel%22%2C%22productDurationEnum%22%2C%22entityTypeDescription%22%2C%22partners%22%2C%22allLanguages%22%5D&tagFilters="}]}
api_endpoint = "https://lua9b20g37-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia for vanilla JavaScript (lite) 3.30.0;react-instantsearch 5.2.3;JS Helper 2.26.1&x-algolia-application-id=LUA9B20G37&x-algolia-api-key=dcc55281ffd7ba6f24c3a9b18288499b"

r = requests.post(api_endpoint, headers=headers, json=payload).json()
data = r['results'][1]['hits']
for course in data:
    print(f"{course['name']} - https://www.coursera.org{course['objectUrl']}")