# Document Delete(Element Id) Method

Source: https://www.revitapidocs.com/2026/a0461dd1-71d9-4581-1604-2ef8c211dd60.htm

---

| Document Delete(Element Id) Method |
| --- |

Deletes an element from the document given the id of that element. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public ICollection<ElementId> Delete(
	ElementId elementId
)
```

```
Public Function Delete ( 
	elementId As ElementId
) As ICollection(Of ElementId)
```

```
public:
ICollection<ElementId^>^ Delete(
	ElementId^ elementId
)
```

```
member Delete : 
        elementId : ElementId -> ICollection<ElementId> 
```

#### Parameters

elementId [ElementId](Element-Id-Class.md)
:   Id of the element to delete.

#### Return Value

ICollection [ElementId](Element-Id-Class.md) 
The deleted element id set. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The element elementId does not exist in the document  \-or\-  ElementId cannot be deleted. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |
| [ModificationForbiddenException](53205486-5917-7c33-8e67-e362106ddc97.htm) | The document is in failure mode: an operation has failed,  and Revit requires the user to either cancel the operation  or fix the problem (usually by deleting certain elements).  \-or\-  The document is being loaded, or is in the midst of another  sensitive process. |
| [ModificationOutsideTransactionException](8f025460-c283-ea99-aa8a-5a36e11528f4.htm) | The document has no open transaction. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks This method will delete the element and any elements that are totally dependent upon that element. Any references to the deleted elements will become invalid and hence cause an exception to be thrown if they are accessed.
 The elements will be deleted with no prompts for user confirmation. If pinned elements cannot be deleted before being unpinned, an exception will be thrown. Note: in a family document, the predefined elements (those elements inherited from its family template file) can't be deleted by this method. 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Document Class](Document-Class.md) [Delete Overload](dd023de2-cf2b-03ca-6f45-89b5e867fe92.htm) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
