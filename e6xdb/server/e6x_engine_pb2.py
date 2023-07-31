# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: e6x_engine.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10\x65\x36x_engine.proto\"2\n\nGFieldInfo\x12\x11\n\tfieldName\x18\x01 \x01(\t\x12\x11\n\tfieldType\x18\x02 \x01(\t\"A\n\x13\x46\x61iledSchemaElement\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x0e\n\x06reason\x18\x03 \x01(\t\"P\n\x16GetAddCatalogsResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\x12&\n\x08\x66\x61ilures\x18\x02 \x03(\x0b\x32\x14.FailedSchemaElement\"2\n\x0f\x43\x61talogResponse\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tisDefault\x18\x02 \x01(\x08\"<\n\x0eParameterValue\x12\r\n\x05index\x18\x01 \x01(\x11\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\t\"D\n\x0c\x43learRequest\x12\x10\n\x08\x65ngineIP\x18\x01 \x01(\t\x12\x11\n\tsessionId\x18\x02 \x01(\t\x12\x0f\n\x07queryId\x18\x03 \x01(\t\"\x0f\n\rClearResponse\"J\n\x12\x43\x61ncelQueryRequest\x12\x10\n\x08\x65ngineIP\x18\x01 \x01(\t\x12\x11\n\tsessionId\x18\x02 \x01(\t\x12\x0f\n\x07queryId\x18\x03 \x01(\t\"\x15\n\x13\x43\x61ncelQueryResponse\"F\n\x0e\x45xplainRequest\x12\x10\n\x08\x65ngineIP\x18\x01 \x01(\t\x12\x11\n\tsessionId\x18\x02 \x01(\t\x12\x0f\n\x07queryId\x18\x03 \x01(\t\"\"\n\x0f\x45xplainResponse\x12\x0f\n\x07\x65xplain\x18\x01 \x01(\t\"Y\n\rDryRunRequest\x12\x10\n\x08\x65ngineIP\x18\x01 \x01(\t\x12\x11\n\tsessionId\x18\x02 \x01(\t\x12\x0e\n\x06schema\x18\x03 \x01(\t\x12\x13\n\x0bqueryString\x18\x04 \x01(\t\"%\n\x0e\x44ryRunResponse\x12\x13\n\x0b\x64ryrunValue\x18\x01 \x01(\t\"l\n\x0f\x44ryRunRequestV2\x12\x10\n\x08\x65ngineIP\x18\x01 \x01(\t\x12\x11\n\tsessionId\x18\x02 \x01(\t\x12\x0e\n\x06schema\x18\x03 \x01(\t\x12\x13\n\x0bqueryString\x18\x04 \x01(\t\x12\x0f\n\x07\x63\x61talog\x18\x05 \x01(\t\"M\n\x15\x45xplainAnalyzeRequest\x12\x10\n\x08\x65ngineIP\x18\x01 \x01(\t\x12\x11\n\tsessionId\x18\x02 \x01(\t\x12\x0f\n\x07queryId\x18\x03 \x01(\t\"0\n\x16\x45xplainAnalyzeResponse\x12\x16\n\x0e\x65xplainAnalyze\x18\x01 \x01(\t\"Q\n\x17PrepareStatementRequest\x12\x11\n\tsessionId\x18\x01 \x01(\t\x12\x0e\n\x06schema\x18\x02 \x01(\t\x12\x13\n\x0bqueryString\x18\x03 \x01(\t\"d\n\x19PrepareStatementV2Request\x12\x11\n\tsessionId\x18\x01 \x01(\t\x12\x0e\n\x06schema\x18\x02 \x01(\t\x12\x13\n\x0bqueryString\x18\x03 \x01(\t\x12\x0f\n\x07\x63\x61talog\x18\x04 \x01(\t\"=\n\x18PrepareStatementResponse\x12\x10\n\x08\x65ngineIP\x18\x01 \x01(\t\x12\x0f\n\x07queryId\x18\x02 \x01(\t\"@\n\x0eUserAccessInfo\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12\x10\n\x08userName\x18\x02 \x01(\t\x12\x0e\n\x06tokens\x18\x03 \x03(\t\"O\n\x17\x45xecuteStatementRequest\x12\x10\n\x08\x65ngineIP\x18\x01 \x01(\t\x12\x11\n\tsessionId\x18\x02 \x01(\t\x12\x0f\n\x07queryId\x18\x03 \x01(\t\"r\n\x19\x45xecuteStatementV2Request\x12\x10\n\x08\x65ngineIP\x18\x01 \x01(\t\x12\x11\n\tsessionId\x18\x02 \x01(\t\x12\x0f\n\x07queryId\x18\x03 \x01(\t\x12\x1f\n\x06params\x18\x04 \x03(\x0b\x32\x0f.ParameterValue\"\x1a\n\x18\x45xecuteStatementResponse\"O\n\x17GetNextResultRowRequest\x12\x10\n\x08\x65ngineIP\x18\x01 \x01(\t\x12\x11\n\tsessionId\x18\x02 \x01(\t\x12\x0f\n\x07queryId\x18\x03 \x01(\t\"-\n\x18GetNextResultRowResponse\x12\x11\n\tresultRow\x18\x02 \x01(\x0c\"Q\n\x19GetNextResultBatchRequest\x12\x10\n\x08\x65ngineIP\x18\x01 \x01(\t\x12\x11\n\tsessionId\x18\x02 \x01(\t\x12\x0f\n\x07queryId\x18\x03 \x01(\t\"1\n\x1aGetNextResultBatchResponse\x12\x13\n\x0bresultBatch\x18\x02 \x01(\x0c\"P\n\x18GetResultMetadataRequest\x12\x10\n\x08\x65ngineIP\x18\x01 \x01(\t\x12\x11\n\tsessionId\x18\x02 \x01(\t\x12\x0f\n\x07queryId\x18\x03 \x01(\t\"3\n\x19GetResultMetadataResponse\x12\x16\n\x0eresultMetaData\x18\x01 \x01(\x0c\"5\n\x13\x41uthenticateRequest\x12\x0c\n\x04user\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\")\n\x14\x41uthenticateResponse\x12\x11\n\tsessionId\x18\x01 \x01(\t\"5\n\x10GetTablesRequest\x12\x11\n\tsessionId\x18\x01 \x01(\t\x12\x0e\n\x06schema\x18\x02 \x01(\t\"H\n\x12GetTablesV2Request\x12\x11\n\tsessionId\x18\x01 \x01(\t\x12\x0e\n\x06schema\x18\x02 \x01(\t\x12\x0f\n\x07\x63\x61talog\x18\x03 \x01(\t\"#\n\x11GetTablesResponse\x12\x0e\n\x06tables\x18\x01 \x03(\t\"*\n\x15GetSchemaNamesRequest\x12\x11\n\tsessionId\x18\x01 \x01(\t\"=\n\x17GetSchemaNamesV2Request\x12\x11\n\tsessionId\x18\x01 \x01(\t\x12\x0f\n\x07\x63\x61talog\x18\x02 \x01(\t\")\n\x16GetSchemaNamesResponse\x12\x0f\n\x07schemas\x18\x01 \x03(\t\"E\n\x11GetColumnsRequest\x12\x11\n\tsessionId\x18\x01 \x01(\t\x12\x0e\n\x06schema\x18\x02 \x01(\t\x12\r\n\x05table\x18\x03 \x01(\t\"X\n\x13GetColumnsV2Request\x12\x11\n\tsessionId\x18\x01 \x01(\t\x12\x0e\n\x06schema\x18\x02 \x01(\t\x12\r\n\x05table\x18\x03 \x01(\t\x12\x0f\n\x07\x63\x61talog\x18\x04 \x01(\t\"4\n\x12GetColumnsResponse\x12\x1e\n\tfieldInfo\x18\x01 \x03(\x0b\x32\x0b.GFieldInfo\"E\n\rStatusRequest\x12\x10\n\x08\x65ngineIP\x18\x01 \x01(\t\x12\x11\n\tsessionId\x18\x02 \x01(\t\x12\x0f\n\x07queryId\x18\x03 \x01(\t\"2\n\x0eStatusResponse\x12\x0e\n\x06status\x18\x02 \x01(\x08\x12\x10\n\x08rowCount\x18\x03 \x01(\x12\"5\n\x12\x41\x64\x64\x43\x61talogsRequest\x12\x11\n\tsessionId\x18\x01 \x01(\t\x12\x0c\n\x04json\x18\x02 \x01(\t\"#\n\x12UpdateUsersRequest\x12\r\n\x05users\x18\x01 \x01(\x0c\"\x15\n\x13UpdateUsersResponse\"3\n\x0fSetPropsRequest\x12\x11\n\tsessionId\x18\x01 \x01(\t\x12\r\n\x05props\x18\x02 \x01(\t\"\x12\n\x10SetPropsResponse\"*\n\x15GetAddCatalogsRequest\x12\x11\n\tsessionId\x18\x01 \x01(\t\"\x15\n\x13\x41\x64\x64\x43\x61talogsResponse\"\x15\n\x13GetCatalogesRequest\"B\n\x14GetCatalogesResponse\x12*\n\x10\x63\x61talogResponses\x18\x01 \x03(\x0b\x32\x10.CatalogResponse\"+\n\x16RefreshCatalogsRequest\x12\x11\n\tsessionId\x18\x01 \x01(\t\"\x19\n\x17RefreshCatalogsResponse\"X\n\x12RemoteChunkRequest\x12\x17\n\x0foriginalQueryId\x18\x01 \x01(\t\x12\x15\n\rremoteQueryId\x18\x02 \x01(\t\x12\x12\n\nsQueryHash\x18\x03 \x01(\t\"3\n\x13RemoteChunkResponse\x12\r\n\x05\x65rror\x18\x01 \x01(\t\x12\r\n\x05\x63hunk\x18\x02 \x01(\x0c\x32\xdb\r\n\x12QueryEngineService\x12&\n\x05\x63lear\x12\r.ClearRequest\x1a\x0e.ClearResponse\x12\x38\n\x0b\x63\x61ncelQuery\x12\x13.CancelQueryRequest\x1a\x14.CancelQueryResponse\x12,\n\x07\x65xplain\x12\x0f.ExplainRequest\x1a\x10.ExplainResponse\x12)\n\x06\x64ryRun\x12\x0e.DryRunRequest\x1a\x0f.DryRunResponse\x12-\n\x08\x64ryRunV2\x12\x10.DryRunRequestV2\x1a\x0f.DryRunResponse\x12\x41\n\x0e\x65xplainAnalyze\x12\x16.ExplainAnalyzeRequest\x1a\x17.ExplainAnalyzeResponse\x12G\n\x10prepareStatement\x12\x18.PrepareStatementRequest\x1a\x19.PrepareStatementResponse\x12K\n\x12prepareStatementV2\x12\x1a.PrepareStatementV2Request\x1a\x19.PrepareStatementResponse\x12G\n\x10\x65xecuteStatement\x12\x18.ExecuteStatementRequest\x1a\x19.ExecuteStatementResponse\x12K\n\x12\x65xecuteStatementV2\x12\x1a.ExecuteStatementV2Request\x1a\x19.ExecuteStatementResponse\x12G\n\x10getNextResultRow\x12\x18.GetNextResultRowRequest\x1a\x19.GetNextResultRowResponse\x12M\n\x12getNextResultBatch\x12\x1a.GetNextResultBatchRequest\x1a\x1b.GetNextResultBatchResponse\x12J\n\x11getResultMetadata\x12\x19.GetResultMetadataRequest\x1a\x1a.GetResultMetadataResponse\x12;\n\x0c\x61uthenticate\x12\x14.AuthenticateRequest\x1a\x15.AuthenticateResponse\x12\x32\n\tgetTables\x12\x11.GetTablesRequest\x1a\x12.GetTablesResponse\x12\x36\n\x0bgetTablesV2\x12\x13.GetTablesV2Request\x1a\x12.GetTablesResponse\x12\x41\n\x0egetSchemaNames\x12\x16.GetSchemaNamesRequest\x1a\x17.GetSchemaNamesResponse\x12\x45\n\x10getSchemaNamesV2\x12\x18.GetSchemaNamesV2Request\x1a\x17.GetSchemaNamesResponse\x12\x35\n\ngetColumns\x12\x12.GetColumnsRequest\x1a\x13.GetColumnsResponse\x12\x39\n\x0cgetColumnsV2\x12\x14.GetColumnsV2Request\x1a\x13.GetColumnsResponse\x12\x38\n\x0bupdateUsers\x12\x13.UpdateUsersRequest\x1a\x14.UpdateUsersResponse\x12/\n\x08setProps\x12\x10.SetPropsRequest\x1a\x11.SetPropsResponse\x12)\n\x06status\x12\x0e.StatusRequest\x1a\x0f.StatusResponse\x12\x38\n\x0b\x61\x64\x64\x43\x61talogs\x12\x13.AddCatalogsRequest\x1a\x14.AddCatalogsResponse\x12I\n\x16getAddCatalogsResponse\x12\x16.GetAddCatalogsRequest\x1a\x17.GetAddCatalogsResponse\x12;\n\x0cgetCataloges\x12\x14.GetCatalogesRequest\x1a\x15.GetCatalogesResponse\x12\x45\n\x18getNextRemoteCachedChunk\x12\x13.RemoteChunkRequest\x1a\x14.RemoteChunkResponse\x12\x44\n\x0frefreshCatalogs\x12\x17.RefreshCatalogsRequest\x1a\x18.RefreshCatalogsResponseB\x02P\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'e6x_engine_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'P\001'
  _globals['_GFIELDINFO']._serialized_start=20
  _globals['_GFIELDINFO']._serialized_end=70
  _globals['_FAILEDSCHEMAELEMENT']._serialized_start=72
  _globals['_FAILEDSCHEMAELEMENT']._serialized_end=137
  _globals['_GETADDCATALOGSRESPONSE']._serialized_start=139
  _globals['_GETADDCATALOGSRESPONSE']._serialized_end=219
  _globals['_CATALOGRESPONSE']._serialized_start=221
  _globals['_CATALOGRESPONSE']._serialized_end=271
  _globals['_PARAMETERVALUE']._serialized_start=273
  _globals['_PARAMETERVALUE']._serialized_end=333
  _globals['_CLEARREQUEST']._serialized_start=335
  _globals['_CLEARREQUEST']._serialized_end=403
  _globals['_CLEARRESPONSE']._serialized_start=405
  _globals['_CLEARRESPONSE']._serialized_end=420
  _globals['_CANCELQUERYREQUEST']._serialized_start=422
  _globals['_CANCELQUERYREQUEST']._serialized_end=496
  _globals['_CANCELQUERYRESPONSE']._serialized_start=498
  _globals['_CANCELQUERYRESPONSE']._serialized_end=519
  _globals['_EXPLAINREQUEST']._serialized_start=521
  _globals['_EXPLAINREQUEST']._serialized_end=591
  _globals['_EXPLAINRESPONSE']._serialized_start=593
  _globals['_EXPLAINRESPONSE']._serialized_end=627
  _globals['_DRYRUNREQUEST']._serialized_start=629
  _globals['_DRYRUNREQUEST']._serialized_end=718
  _globals['_DRYRUNRESPONSE']._serialized_start=720
  _globals['_DRYRUNRESPONSE']._serialized_end=757
  _globals['_DRYRUNREQUESTV2']._serialized_start=759
  _globals['_DRYRUNREQUESTV2']._serialized_end=867
  _globals['_EXPLAINANALYZEREQUEST']._serialized_start=869
  _globals['_EXPLAINANALYZEREQUEST']._serialized_end=946
  _globals['_EXPLAINANALYZERESPONSE']._serialized_start=948
  _globals['_EXPLAINANALYZERESPONSE']._serialized_end=996
  _globals['_PREPARESTATEMENTREQUEST']._serialized_start=998
  _globals['_PREPARESTATEMENTREQUEST']._serialized_end=1079
  _globals['_PREPARESTATEMENTV2REQUEST']._serialized_start=1081
  _globals['_PREPARESTATEMENTV2REQUEST']._serialized_end=1181
  _globals['_PREPARESTATEMENTRESPONSE']._serialized_start=1183
  _globals['_PREPARESTATEMENTRESPONSE']._serialized_end=1244
  _globals['_USERACCESSINFO']._serialized_start=1246
  _globals['_USERACCESSINFO']._serialized_end=1310
  _globals['_EXECUTESTATEMENTREQUEST']._serialized_start=1312
  _globals['_EXECUTESTATEMENTREQUEST']._serialized_end=1391
  _globals['_EXECUTESTATEMENTV2REQUEST']._serialized_start=1393
  _globals['_EXECUTESTATEMENTV2REQUEST']._serialized_end=1507
  _globals['_EXECUTESTATEMENTRESPONSE']._serialized_start=1509
  _globals['_EXECUTESTATEMENTRESPONSE']._serialized_end=1535
  _globals['_GETNEXTRESULTROWREQUEST']._serialized_start=1537
  _globals['_GETNEXTRESULTROWREQUEST']._serialized_end=1616
  _globals['_GETNEXTRESULTROWRESPONSE']._serialized_start=1618
  _globals['_GETNEXTRESULTROWRESPONSE']._serialized_end=1663
  _globals['_GETNEXTRESULTBATCHREQUEST']._serialized_start=1665
  _globals['_GETNEXTRESULTBATCHREQUEST']._serialized_end=1746
  _globals['_GETNEXTRESULTBATCHRESPONSE']._serialized_start=1748
  _globals['_GETNEXTRESULTBATCHRESPONSE']._serialized_end=1797
  _globals['_GETRESULTMETADATAREQUEST']._serialized_start=1799
  _globals['_GETRESULTMETADATAREQUEST']._serialized_end=1879
  _globals['_GETRESULTMETADATARESPONSE']._serialized_start=1881
  _globals['_GETRESULTMETADATARESPONSE']._serialized_end=1932
  _globals['_AUTHENTICATEREQUEST']._serialized_start=1934
  _globals['_AUTHENTICATEREQUEST']._serialized_end=1987
  _globals['_AUTHENTICATERESPONSE']._serialized_start=1989
  _globals['_AUTHENTICATERESPONSE']._serialized_end=2030
  _globals['_GETTABLESREQUEST']._serialized_start=2032
  _globals['_GETTABLESREQUEST']._serialized_end=2085
  _globals['_GETTABLESV2REQUEST']._serialized_start=2087
  _globals['_GETTABLESV2REQUEST']._serialized_end=2159
  _globals['_GETTABLESRESPONSE']._serialized_start=2161
  _globals['_GETTABLESRESPONSE']._serialized_end=2196
  _globals['_GETSCHEMANAMESREQUEST']._serialized_start=2198
  _globals['_GETSCHEMANAMESREQUEST']._serialized_end=2240
  _globals['_GETSCHEMANAMESV2REQUEST']._serialized_start=2242
  _globals['_GETSCHEMANAMESV2REQUEST']._serialized_end=2303
  _globals['_GETSCHEMANAMESRESPONSE']._serialized_start=2305
  _globals['_GETSCHEMANAMESRESPONSE']._serialized_end=2346
  _globals['_GETCOLUMNSREQUEST']._serialized_start=2348
  _globals['_GETCOLUMNSREQUEST']._serialized_end=2417
  _globals['_GETCOLUMNSV2REQUEST']._serialized_start=2419
  _globals['_GETCOLUMNSV2REQUEST']._serialized_end=2507
  _globals['_GETCOLUMNSRESPONSE']._serialized_start=2509
  _globals['_GETCOLUMNSRESPONSE']._serialized_end=2561
  _globals['_STATUSREQUEST']._serialized_start=2563
  _globals['_STATUSREQUEST']._serialized_end=2632
  _globals['_STATUSRESPONSE']._serialized_start=2634
  _globals['_STATUSRESPONSE']._serialized_end=2684
  _globals['_ADDCATALOGSREQUEST']._serialized_start=2686
  _globals['_ADDCATALOGSREQUEST']._serialized_end=2739
  _globals['_UPDATEUSERSREQUEST']._serialized_start=2741
  _globals['_UPDATEUSERSREQUEST']._serialized_end=2776
  _globals['_UPDATEUSERSRESPONSE']._serialized_start=2778
  _globals['_UPDATEUSERSRESPONSE']._serialized_end=2799
  _globals['_SETPROPSREQUEST']._serialized_start=2801
  _globals['_SETPROPSREQUEST']._serialized_end=2852
  _globals['_SETPROPSRESPONSE']._serialized_start=2854
  _globals['_SETPROPSRESPONSE']._serialized_end=2872
  _globals['_GETADDCATALOGSREQUEST']._serialized_start=2874
  _globals['_GETADDCATALOGSREQUEST']._serialized_end=2916
  _globals['_ADDCATALOGSRESPONSE']._serialized_start=2918
  _globals['_ADDCATALOGSRESPONSE']._serialized_end=2939
  _globals['_GETCATALOGESREQUEST']._serialized_start=2941
  _globals['_GETCATALOGESREQUEST']._serialized_end=2962
  _globals['_GETCATALOGESRESPONSE']._serialized_start=2964
  _globals['_GETCATALOGESRESPONSE']._serialized_end=3030
  _globals['_REFRESHCATALOGSREQUEST']._serialized_start=3032
  _globals['_REFRESHCATALOGSREQUEST']._serialized_end=3075
  _globals['_REFRESHCATALOGSRESPONSE']._serialized_start=3077
  _globals['_REFRESHCATALOGSRESPONSE']._serialized_end=3102
  _globals['_REMOTECHUNKREQUEST']._serialized_start=3104
  _globals['_REMOTECHUNKREQUEST']._serialized_end=3192
  _globals['_REMOTECHUNKRESPONSE']._serialized_start=3194
  _globals['_REMOTECHUNKRESPONSE']._serialized_end=3245
  _globals['_QUERYENGINESERVICE']._serialized_start=3248
  _globals['_QUERYENGINESERVICE']._serialized_end=5003
# @@protoc_insertion_point(module_scope)
