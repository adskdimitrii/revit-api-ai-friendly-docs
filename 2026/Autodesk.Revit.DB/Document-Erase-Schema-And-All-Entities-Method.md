# Document Erase Schema And All Entities Method

Source: https://www.revitapidocs.com/2026/50debcb0-3c4f-b32b-2edb-8a6ef7b4bf8d.htm

---

| Document Erase Schema And All Entities Method |
| --- |

Erases Schema and all its Entities from the document. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public void EraseSchemaAndAllEntities(
	Schema schema
)
```

```
Public Sub EraseSchemaAndAllEntities ( 
	schema As Schema
)
```

```
public:
void EraseSchemaAndAllEntities(
	Schema^ schema
)
```

```
member EraseSchemaAndAllEntities : 
        schema : Schema -> unit 
```

#### Parameters

schema [Schema](9817e7db-8367-ea4e-1769-0488f3faa37f.htm)
:   The Schema to erase.

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | No write access to this Schema. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |
| [ModificationForbiddenException](53205486-5917-7c33-8e67-e362106ddc97.htm) | The document is in failure mode: an operation has failed,  and Revit requires the user to either cancel the operation  or fix the problem (usually by deleting certain elements).  \-or\-  The document is being loaded, or is in the midst of another  sensitive process. |
| [ModificationOutsideTransactionException](8f025460-c283-ea99-aa8a-5a36e11528f4.htm) | The document has no open transaction. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks The Schema remains in memory. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Document Class](Document-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
