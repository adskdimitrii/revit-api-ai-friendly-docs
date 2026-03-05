# Element Id Compare To Method

Source: https://www.revitapidocs.com/2026/bb0270fb-af8b-95ed-31c9-6f233dba4461.htm

---

| Element Id Compare To Method |
| --- |

Compares two element ids. Implementation of System.IComparable interface 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public virtual int CompareTo(
	Object id
)
```

```
Public Overridable Function CompareTo ( 
	id As Object
) As Integer
```

```
public:
virtual int CompareTo(
	Object^ id
)
```

```
abstract CompareTo : 
        id : Object -> int 
override CompareTo : 
        id : Object -> int 
```

#### Parameters

id Object
:   The ElementId to be compared with this ElementId.

#### Return Value

Int32 
\-1 if this element id is less than other id, 0 if equal, 1 if greater. 

#### Implements

IComparable CompareTo(Object) 
![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[ElementId Class](Element-Id-Class.md) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
