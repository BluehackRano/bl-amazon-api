from swagger_server.models.get_tool_titles_response import GetToolTitlesResponse
from swagger_server.models.get_tool_titles_response_data import GetToolTitlesResponseData

from swagger_server.models.get_dictionary_words_response import GetDictionaryWordsResponse
from swagger_server.models.get_dictionary_words_response_data import GetDictionaryWordsResponseData

from swagger_server.models.get_dictionary_words_filtered_response import GetDictionaryWordsFilteredResponse
from swagger_server.models.get_dictionary_words_filtered_response_data import GetDictionaryWordsFilteredResponseData
from swagger_server.models.get_dictionary_words_filtered_response_data_words import GetDictionaryWordsFilteredResponseDataWords

from bl_db_product_amz_best.products import Products
from bl_title_amaz.title_filter import Title_filter

from collections import Counter

class Tool(object):
  def __init__(self):
    super().__init__()

  @staticmethod
  def get_tool_titles(nodeId):
    api_instance = Products()
    res = GetToolTitlesResponse()

    try:
      res_data = GetToolTitlesResponseData()

      offset = 0
      limit = 100

      products_res = api_instance.get_products_by_node_id(node_id=nodeId, offset=offset, limit=limit)
      if products_res:
        if len(products_res) > 0:
          title_list = []
          for product in products_res:
            title_list.append(product.get('Title'))
          res_data.titles = title_list
        res.data = res_data
        res.message = 'Successful'
        response_status = 200
      else:
        res.message = 'No products'
        response_status = 400

    except Exception as e:
      res.message = str(e)
      response_status = 400

    return res, response_status

  @staticmethod
  def get_dictionary_words(nodeIds):
    api_instance = Title_filter()
    res = GetDictionaryWordsResponse()

    try:
      res_data = GetDictionaryWordsResponseData()

      word_res = api_instance.get_title_word_dic_by_node_id(node_ids=nodeIds)
      if word_res:
        if len(word_res) > 0:
          word_list = []
          for word in word_res:
            word_list.append(word)
          res_data.words = word_list
          res.data = res_data
          res.message = 'Successful'
          response_status = 200
        else:
          res.message = 'No words'
          response_status = 400
      else:
        res.message = 'No words'
        response_status = 400

    except Exception as e:
      res.message = str(e)
      response_status = 400

    return res, response_status

  @staticmethod
  def get_dictionary_words_filtered(nodeId, filters):
    api_instance = Title_filter()
    res = GetDictionaryWordsFilteredResponse()

    try:
      res_data = GetDictionaryWordsFilteredResponseData()

      filtered_titles, result_word = api_instance.filtering_titles(node_ids=[nodeId], filter_list=filters)
      if result_word:
        if len(result_word) > 0:
          word_list = []
          for k, v in result_word.most_common():
            word = GetDictionaryWordsFilteredResponseDataWords()
            word.text = k
            word.count = v
            word_list.append(word)
          res_data.words = word_list
          res.data = res_data
          res.message = 'Successful'
          response_status = 200
        else:
          res.message = 'No words'
          response_status = 400
      else:
        res.message = 'No words'
        response_status = 400

    except Exception as e:
      res.message = str(e)
      response_status = 400

    return res, response_status

  @staticmethod
  def post_dictionary_products_attrs_sub_attrs(nodeId, attrId, subAttrId, subAttrUsName, subAttrKrName, attrUsName=None, attrKrName=None):
    return

  @staticmethod
  def post_dictionary_words(subAttrId, word):
    return
