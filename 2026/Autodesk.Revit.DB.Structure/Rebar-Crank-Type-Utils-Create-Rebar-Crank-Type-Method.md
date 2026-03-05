# Rebar Crank Type Utils Create Rebar Crank Type Method

Source: https://www.revitapidocs.com/2026/a1bbebb5-4b7d-75ea-ff6d-effd80f3f681.htm

---

| Rebar Crank Type Utils Create Rebar Crank Type Method |
| --- |

Creates a Rebar Crank Type element. 
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public static ElementType CreateRebarCrankType(
	Document document,
	string typeName
)
```

```
Public Shared Function CreateRebarCrankType ( 
	document As Document,
	typeName As String
) As ElementType
```

```
public:
static ElementType^ CreateRebarCrankType(
	Document^ document, 
	String^ typeName
)
```

```
static member CreateRebarCrankType : 
        document : Document * 
        typeName : string -> ElementType 
```

#### Parameters

document [Document](../Autodesk.Revit.DB/Document-Class.md)
:   The document.

typeName String
:   The Rebar Crank Type name.

#### Return Value

[ElementType](../Autodesk.Revit.DB/Element-Type-Class.md) 
The Rebar Crank Type. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | The given value for typeName cannot be an empty string.  \-or\-  The given value for typeName cannot include prohibited characters.  \-or\-  The given value for typeName is already in use by another Rebar Crank Type. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[RebarCrankTypeUtils Class](Rebar-Crank-Type-Utils-Class.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
