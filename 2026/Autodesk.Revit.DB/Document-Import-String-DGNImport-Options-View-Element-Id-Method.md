# Document Import(String, DGNImport Options, View, Element Id ) Method

Source: https://www.revitapidocs.com/2026/8e1bc344-210c-b202-8f37-8197b781beff.htm

---

| Document Import(String, DGNImport Options, View, Element Id ) Method |
| --- |

Imports a DGN file to the document. 
**Namespace:** [Autodesk.Revit.DB](../ungrouped/Autodesk.-Revit.-DB-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public bool Import(
	string file,
	DGNImportOptions options,
	View pDBView,
	out ElementId elementId
)
```

```
Public Function Import ( 
	file As String,
	options As DGNImportOptions,
	pDBView As View,
	<OutAttribute> ByRef elementId As ElementId
) As Boolean
```

```
public:
bool Import(
	String^ file, 
	DGNImportOptions^ options, 
	View^ pDBView, 
	[OutAttribute] ElementId^% elementId
)
```

```
member Import : 
        file : string * 
        options : DGNImportOptions * 
        pDBView : View * 
        elementId : ElementId byref -> bool 
```

#### Parameters

file String
:   Full path of the file to import. File must exist and must be a valid DGN file.

options [DGNImportOptions](81dec13f-8eca-f2eb-bf60-1e206e6d0d98.htm)
:   Various options applicable to the DGN format. If , all options will be set to their respective default values.

pDBView [View](View-Class.md)
:   View used to aid placement of the imported file. If the options specify ThisViewOnly, this argument is required and the imported file
 will only be visible in the specified view. If the options specify center\-to\-center placement, this argument is required and the imported
 file will be placed in the center of the specified view. Otherwise, this view is used to obtain a base level to associate with the imported
 file. If not specified, an existing view will be chosen instead and may open a view or associate the imported file to an arbitrary level.

elementId [ElementId](Element-Id-Class.md)
:   The id of imported instance after a successful import.

#### Return Value

Boolean 
True if successful, otherwise False. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Exceptions 

| Exception | Condition |
| --- | --- |
| [ArgumentException](2e6e4206-97a8-dd4b-df5d-4269f4bb6088.htm) | Not a valid file for DGN import (.dgn files are valid).  \-or\-  ThisViewOnly cannot be true when importing a DWG\|DGN drawing into a 3D view.  \-or\-  The provided view is not valid for the options provided.  \-or\-  One or more strings describing layer selection is invalid or empty.  \-or\-  The scale is not valid as a CustomScale for use during import.  \-or\-  NullOrEmpty  \-or\-  The view is not printable.  \-or\-  Empty DGN model view name characters.  \-or\-  Visible layer only option must be set to false for DGN import. |
| [ArgumentNullException](631e1424-60f4-929b-4e52-dda9dcd26316.htm) | A non\-optional argument was null |
| [FileArgumentNotFoundException](ca9ccaa9-ed08-d40d-31a7-1af3ad2dcb84.htm) | The given file does not exist. |
| [InvalidOperationException](9e715f03-3884-e539-4dd6-8d7545733adc.htm) | Import is temporarily disabled. |
| [ModificationForbiddenException](53205486-5917-7c33-8e67-e362106ddc97.htm) | The document is in failure mode: an operation has failed,  and Revit requires the user to either cancel the operation  or fix the problem (usually by deleting certain elements).  \-or\-  The document is being loaded, or is in the midst of another  sensitive process. |
| [ModificationOutsideTransactionException](8f025460-c283-ea99-aa8a-5a36e11528f4.htm) | The document has no open transaction. |
| [OptionalFunctionalityNotAvailableException](0612a676-b6ba-8c37-2e28-b197438305ab.htm) | The Material Library is missing in the installed Revit.  \-or\-  The DGN Import/Link module is not available in the installed Revit. |

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Document Class](Document-Class.md) [Import Overload](05c3dbe2-fe7e-c293-761d-b11f356a011b.htm) [Autodesk.Revit.DB Namespace](../ungrouped/Autodesk.-Revit.-DB-Namespace.md)
