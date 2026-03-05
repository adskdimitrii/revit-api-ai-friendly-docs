# Rebar Create Free Form(Document, Rebar Bar Type, Element, IList IList Curve , Rebar Style) Method

Source: https://www.revitapidocs.com/2026/aec398ad-d9c3-b85c-c5f5-fec5dc068831.htm

---

| Rebar Create Free Form(Document, Rebar Bar Type, Element, IList IList Curve , Rebar Style) Method |
| --- |

  
**Namespace:** [Autodesk.Revit.DB.Structure](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public static RebarFreeFormCreationResult CreateFreeForm(
	Document doc,
	RebarBarType barType,
	Element host,
	IList<IList<Curve>> curves,
	RebarStyle style
)
```

```
Public Shared Function CreateFreeForm ( 
	doc As Document,
	barType As RebarBarType,
	host As Element,
	curves As IList(Of IList(Of Curve)),
	style As RebarStyle
) As RebarFreeFormCreationResult
```

```
public:
static RebarFreeFormCreationResult^ CreateFreeForm(
	Document^ doc, 
	RebarBarType^ barType, 
	Element^ host, 
	IList<IList<Curve^>^>^ curves, 
	RebarStyle style
)
```

```
static member CreateFreeForm : 
        doc : Document * 
        barType : RebarBarType * 
        host : Element * 
        curves : IList<IList<Curve>> * 
        style : RebarStyle -> RebarFreeFormCreationResult 
```

#### Parameters

doc [Document](../Autodesk.Revit.DB/Document-Class.md)
barType [RebarBarType](Rebar-Bar-Type-Class.md)
host [Element](../Autodesk.Revit.DB/Element-Class.md)
curves IList IList [Curve](../Autodesk.Revit.DB/Curve-Class.md)
style [RebarStyle](a9ac65a6-29e6-25e5-caca-502e21385f47.htm)

#### Return Value

[RebarFreeFormCreationResult](Rebar-Free-Form-Creation-Result-Class.md) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Rebar Class](Rebar-Class.md) [CreateFreeForm Overload](Rebar-Create-Free-Form-Method.md) [Autodesk.Revit.DB.Structure Namespace](../ungrouped/Autodesk.-Revit.-DB.-Structure-Namespace.md)
